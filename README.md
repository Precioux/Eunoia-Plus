
# Eunoia-Plus: Open-Domain Chitchat System

**Eunoia-Plus** is an advanced open-domain chitchat system that integrates multiple AI modules to create dynamic, intelligent, and natural conversations. The system is designed using a multi-module architecture, enabling it to understand and respond to user inputs across a wide range of domains, including weather, currency, and more.

## Features

- **Modular Architecture**: The system is divided into four key modules:
  1. **Natural Language Understanding (NLU)**: Uses a fine-tuned RoBERTa model to detect user intents and extract necessary information with high accuracy.
  2. **Intent Validation**: An XGBoost-based model ensures the correctness of detected intents, handling ambiguous and overlapping intents efficiently.
  3. **Dialogue State Tracking (DST)**: Keeps track of conversation state using both rule-based and GPT-3.5 Turbo methods, offering flexibility in conversation flow management.
  4. **Answer Generation**: Utilizes BLOOM and T5 models to generate coherent and contextually appropriate responses.

- **Support for Various Intent Structures**: Handles four categories of intents:
  1. Intents without slots.
  2. Intents with optional slots.
  3. Intents requiring one essential slot.
  4. Intents requiring multiple essential slots.

- **High Accuracy**: The system delivers high accuracy across several metrics:
  - NLU Module: 96% intent detection accuracy, 97% slot filling accuracy.
  - Intent Validation: 95% accuracy.
  - Dialogue State Tracking: 92% accuracy using rule-based methods, with enhanced contextual accuracy via GPT-based methods.
  - Answer Generation: Produces relevant responses by leveraging the conversation history and state.
  
## Usage

1. The system is built to handle multi-turn conversations based on an open-domain dataset.
2. Users can interact with the system via the command line or integrate it into other conversational platforms or applications.
3. The modular architecture allows for easy customization, making it adaptable to different domains or intents.

## Project Structure

- `nlu/`: Contains code for the Natural Language Understanding module and its data.
- `api/`: Contains api code for calling fine-tuned model as a server.
- `intent_validation/`: XGBoost-based module to validate detected intents.
- `dst/`: Rule-based and GPT-3.5 based dialogue state tracking implementations.
- `answer_generation/`: Answer generation models, including BLOOM and T5.

## Models Used

- **RoBERTa**: For intent detection and slot filling.
- **XGBoost**: For intent validation and ensuring reliable intent resolution.
- **GPT-3.5 Turbo**: For advanced dialogue state tracking using few-shot learning.
- **BLOOM and T5**: For generating contextually relevant responses.

## Performance

The system has been evaluated using several key metrics:
- **Intent Detection**: 96% accuracy.
- **Slot Filling**: 97% accuracy.
- **Intent Validation**: 95% accuracy.
- **Dialogue State Tracking**: 
  - Rule-based: 92% state accuracy.
  - GPT-based: 69.94% overall accuracy (NLU output), 100% fluency (conversation flow).
