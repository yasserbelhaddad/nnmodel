import asyncio
import socket
from py_eureka_client.eureka_client import EurekaClient

def get_ip_address():
    """Get the primary IP address of the local machine."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Connect to an external server to determine the primary network interface
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
    except Exception:
        ip_address = "127.0.0.1"
    finally:
        s.close()
    return ip_address

async def start_eureka_client():
    # Get the local machine's IP address
    ip_address = get_ip_address()
    print("here: "+ip_address)
    # Initialize Eureka client
    eureka_client = EurekaClient(
        eureka_server="https://ntic-discovery-server2.onrender.com/eureka/",
        app_name="price_prediction",
        instance_host=ip_address,
        instance_port=8000,  # The port your Django app is running on
        instance_ip=ip_address,  # The IP address your Django app is running on
        instance_id="price_prediction",
        renewal_interval_in_secs=10,  # Heartbeat interval
        duration_in_secs=90  # Expiry duration
    )

    # Start the Eureka client
    await eureka_client.start()

def run_eureka_client():
    asyncio.run(start_eureka_client())
