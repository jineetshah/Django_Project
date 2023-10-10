from typing import Tuple
from uagents import Agent, Context
from fetcher import fetch_temperature, send_alert
import sys

email = sys.argv[1]
location = sys.argv[2]

# Create the agent object
temperature_agent = Agent(name="temperature_agent",
                          seed="your_recovery_phrase")


# Define the task for the agent to check the temperature and send alerts
@temperature_agent.on_interval(period=3600)  # Run the task every 1 hr
async def check_temperature(ctx: Context):
    global location
    # Fetch the current temperature from the weather API for the specified location
    min_temperature = int(sys.argv[3])
    max_temperature = int(sys.argv[4])

    response = fetch_temperature(location)
    temperature = float(response["temperature_celsius"])

    print(f"Temperature of the location: {temperature}")
    if temperature < min_temperature:
        msg = f"Temperature below minimum threshold: {temperature}°C for {location}"
        ctx.logger.info(msg)
        # Send an alert/notification to the user
        send_alert(email, msg)

    if temperature > max_temperature:
        msg = f"Temperature above maximum threshold: {temperature}°C for {location}"
        ctx.logger.info(msg)
        # Send an alert/notification to the user
        send_alert(email, msg)


if __name__ == "__main__":
    temperature_agent.run()
