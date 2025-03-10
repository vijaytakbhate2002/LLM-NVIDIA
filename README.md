# LLM NVIDIA Streamlit Application

This repository hosts a Streamlit application that calls NVIDIA's `llama-3.1-nemotron-70b-instruct` model on the backend to handle and respond to user queries. Users can enter their questions in a text area, and the model will provide a response directly in the application interface.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [Repository Structure](#repository-structure)
- [License](#license)

## Overview

This application leverages the power of NVIDIA's large language model (`llama-3.1-nemotron-70b-instruct`) to create an interactive query-response experience. It is built using Streamlit to ensure a user-friendly and responsive interface for text-based interactions.

## Features

- **Interactive Query-Response**: A simple text area for inputting queries, with responses displayed directly below.
- **Streamlit-Based UI**: Minimalist and clean design for easy user interaction.
- **Efficient Backend**: NVIDIA's `llama-3.1-nemotron-70b-instruct` model is integrated to deliver highly accurate and contextually relevant responses.

## Installation

To get started, clone the repository and install the dependencies listed in `requirements.txt`:

```bash
# Clone the repository
git clone https://github.com/vijaytakbhate2002/LLM-NVIDIA.git
cd LLM-NVIDIA

# Install dependencies
pip install -r requirements.txt
```

## Usage

To start the Streamlit application, simply run the `app.py` file:

```bash
streamlit run app.py
```

Once the application is running, open a web browser and navigate to the URL provided in the terminal (default is `http://localhost:8501`). 

In the application:
1. Type your query in the provided text area.
2. Click on "Submit" (or press Enter) to receive a response from the NVIDIA model.

## Requirements

The dependencies required for this application are listed in `requirements.txt`. Please ensure your environment meets these requirements before running the app.

## Repository Structure

- **app.py**: Main application file that initializes the Streamlit interface and connects to the NVIDIA model.
- **requirements.txt**: Contains all the Python dependencies required to run the application.

## License

This project is licensed under the MIT License.
