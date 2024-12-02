from llm_axe import Agent, AgentType
import requests

# Custom LLM class using your provided model config
class MyCustomLLM:

    def __init__(self, model, base_url, api_key):
        self.model = model
        self.base_url = base_url
        self.api_key = api_key

    def ask(self, prompts: list, format: str = "", temperature: float = 0.8):
        """
        Sends a request to the external API for the LLM model and retrieves a response.

        Args:
            prompts (list): A list of prompts in OpenAI format (role: system/user/assistant).
            format (str, optional): The format of the response. Defaults to "".
            temperature (float, optional): The temperature for controlling creativity. Defaults to 0.8.

        Returns:
            str: The response from the LLM model.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        # Prepare the payload with the messages instead of prompts
        data = {
            "model": self.model,
            "messages": prompts,  # Now using 'messages' instead of 'prompts'
            "temperature": temperature
        }

        # Send the request to your LLM's API endpoint
        response = requests.post(f"{self.base_url}/completions", json=data, headers=headers)

        # Check for successful response
        if response.status_code == 200:
            return response.json().get("choices", [{}])[0].get("message", {}).get("content", "No response text available")
        else:
            return f"Error: {response.status_code}, {response.text}"

# Initialize the custom LLM with your configuration
llm = MyCustomLLM(
    model="gpt-4o-mini",
    base_url="https://api.avalai.ir/v1",
    api_key="aa-RUo4CAgRbUdZWVXcM6K9rQA4lCLjc8STMetCBR6PEmzEIBhz"
)

# Example OpenAI-style conversation prompts
prompts = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hi, how are you today?"}
]

# Use this custom LLM in an agent
agent = Agent(llm, agent_type=AgentType.GENERIC_RESPONDER)

# Example usage of the agent
response = agent.ask(prompts)
print(response)
