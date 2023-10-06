from typing import Tuple
from uagents import Agent, Context
from fetcher import fetch_temperature, send_alert
import sys

location = sys.argv[1]

# Create the agent object
temperature_agent = Agent(name="temperature_agent",
                          seed="your_recovery_phrase")


# Define the task for the agent to check the temperature and send alerts
@temperature_agent.on_interval(period=30)  # Run the task every 60 seconds
async def check_temperature(ctx: Context):
    global location
    # Fetch the current temperature from the weather API for the specified location
    min_temperature = 30
    max_temperature = 40

    response = fetch_temperature(location)
    temperature = float(response["temperature_celsius"])

    print(f"Temperature of the location: {temperature}")
    if temperature < min_temperature:
        ctx.logger.info(
            f"Temperature below minimum threshold: {temperature}°C")
        # Send an alert/notification to the user
        send_alert("Temperature below minimum threshold")

    if temperature > max_temperature:
        ctx.logger.info(
            f"Temperature above maximum threshold: {temperature}°C")
        # Send an alert/notification to the user
        send_alert("Temperature above maximum threshold")


if __name__ == "__main__":
    temperature_agent.run()
