# EyePop.ai Text Detection Example

This project uses the EyePop.ai API to extract and structure nutrition data from images of nutrition labels.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have Python 3 installed on your machine.
- You have a valid `pop_id` and `secret_key` from EyePop.ai.
- You have installed the necessary Python packages.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/trevorcarr/eyepop.git
    cd eyepop
    ```

2. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

3. Create a [config.py](http://_vscodecontentref_/4) file in the project directory and add your EyePop.ai credentials:

    ```python
    # config.py
    pop_id = 'your_pop_id'
    secret_key = 'your_secret_key'
    ```

4. Create a `.gitignore` file in the project directory to exclude the [config.py](http://_vscodecontentref_/5) file and Python cache files:

    ```plaintext
    # Ignore the config file containing sensitive information
    config.py

    # Ignore Python cache files
    __pycache__/
    ```

## Usage

To run the script and extract nutrition data from an image, use the following command:

```sh
python image_detection.py path/to/your/image.png