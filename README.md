[![GitHub issues](https://img.shields.io/github/issues/CaptioDev/LPMoP)](https://github.com/CaptioDev/LPMoP/issues)
[![GitHub license](https://img.shields.io/github/license/CaptioDev/LPMoP)](https://github.com/CaptioDev/LPMoP/blob/main/LICENSE)
[![Code size](https://img.shields.io/github/languages/code-size/CaptioDev/LPMoP)](https://github.com/CaptioDev/LPMoP)
[![Last commit](https://img.shields.io/github/last-commit/CaptioDev/LPMoP)](https://github.com/CaptioDev/LPMoP/commits/main)
[![Contributors](https://img.shields.io/github/contributors/CaptioDev/LPMoP)](https://github.com/CaptioDev/LPMoP/graphs/contributors)
[![Closed issues](https://img.shields.io/github/issues-closed/CaptioDev/LPMoP)](https://github.com/CaptioDev/LPMoP/issues?q=is%3Aissue+is%3Aclosed)
[![Open pull requests](https://img.shields.io/github/issues-pr/CaptioDev/LPMoP)](https://github.com/CaptioDev/LPMoP/pulls)
[![Watchers](https://img.shields.io/github/watchers/CaptioDev/LPMoP)](https://github.com/CaptioDev/LPMoP/watchers)
[![Release date](https://img.shields.io/github/release-date/CaptioDev/LPMoP)](https://github.com/CaptioDev/LPMoP/releases)



# sNLPM

(sNLPM stands for small Natural Language Processing Model)

sNLPM is a natural language processing model trained on the GPT-2 architecture of AI (artificial intelligence). It can generate human-like text based on the input it receives.

## Features

- Generates text based on given prompts.
- Can be fine-tuned on specific datasets for specialized tasks.
- Easy-to-use interface for interacting with the model.

## Installation

To use sNLPM, follow these steps for Windows 8.1 and above: (THIS IS NOT COMPLETE, PLEASE DO NOT FOLLOW INSTRTUCTIONS UNTIL COMPLETE)

1. Install Python 3.12
   Go to https://www.python.org/downloads/ and find the download for your PC

2. Open cmd and execute:
   ``` bash
   pip
   ```

3. Execute:
   ``` bash
   cls
   ```

4. Execute: (This will take a while)
   ``` bash
   pip install torch torchvision torchaudio
   ```

5. Execute:
   ``` bash
   pip install jupyter
   ```

6. Execute: (This will take a while for the first time only)
   ``` bash
   jupyter notebook
   ```

7. Once in Jupyter Notebook, open a new console and run:
   ``` bash
   git clone https://github.com/CaptioDev/LPMoP.git
   ```

8. Move all files from LPMoP to the main directory

9. In Jupyter Console run:
    ``` bash
    pip install -r requirements.txt
    ```

10. Open a new Notebook

11. In a new cell, run:
``` bash
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load the trained model and tokenizer
model = GPT2LMHeadModel.from_pretrained("lpmop")
tokenizer = GPT2Tokenizer.from_pretrained("lpmop")

# Define a function to generate text based on a prompt
def generate_text(prompt, max_length=200):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(input_ids, max_length=max_length, num_return_sequences=1)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

# Edit the user_input value to change your message prompt
while True:
    user_input = input(" ")
    if user_input.lower() == "exit":
        break
    generated_text = generate_text(user_input, max_length=150)
    print("LPMoP: ", generated_text)
```

## Usage

sNLPM can be used for various purposes such as:

- Generating text for creative writing projects.
- Assisting in content generation for social media or blogs.
- Providing automated responses in chatbots or virtual assistants.

To generate text, simply provide LPMoP with a prompt and it will generate a response based on its training.

## Contributing

If you'd like to contribute to sNLPM, feel free to fork the repository and submit a pull request with your changes. Please adhere to our license,
and contact us for any other questions you might have at: admin@pqar.net.

## License

sNLPM is licensed under CC BY-SA 4.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project uses the [Hugging Face Transformers](https://github.com/huggingface/transformers) library for natural language processing tasks.
- Special thanks to MaskedMatters.
- Thanks to Reddit for providing thousands of pages of training data.
