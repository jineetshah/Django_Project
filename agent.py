from typing import Tuple
from uagents import Agent, Context
from fetcher import fetch_temperature, send_alert

# Create the agent object
temperature_agent = Agent(name="temperature_agent", seed="your_recovery_phrase")

# Define the task for the agent to check the temperature and send alerts
@temperature_agent.on_interval(period=2)  # Run the task every 60 seconds
async def check_temperature(ctx: Context, location: str, range: Tuple[int, int]):
    # Fetch the current temperature from the weather API for the specified location
    min_temperature = 40
    max_temperature = range[1]

    temperature = fetch_temperature(location)

    if temperature < min_temperature:
        ctx.logger.info(f"Temperature below minimum threshold: {temperature}°C")
        # Send an alert/notification to the user
        send_alert("Temperature below minimum threshold")

    if temperature > max_temperature:
        ctx.logger.info(f"Temperature above maximum threshold: {temperature}°C")
        # Send an alert/notification to the user
        send_alert("Temperature above maximum threshold")

if __name__ == "__main__":
    temperature_agent.run()