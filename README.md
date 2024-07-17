# Vidtranslate

## Introduction

Vidtranslate is an application that translates video subtitles to English. It allows users to download both the translated English version and the original subtitles.

## Prerequisites

- This application is developed using Python and Streamlit.
- It is designed to run on Windows. It might work on other operating systems, but this has not been confirmed.

## Installation

### Step 1: Install Chocolatey

Chocolatey is a package manager for Windows. You can install it by following the instructions at [Install Chocolatey](https://chocolatey.org/install#individual).

### Step 2: Install ffmpeg

Once Chocolatey is installed, you can use it to install ffmpeg:

1. Open Command Prompt as an Administrator.
2. Run the following command to install ffmpeg:
   ```cmd
   choco install ffmpeg
   ```

### Step 3: Run the Application

1. Open Command Prompt.
2. Navigate to the directory where your `app.py` file is located.
3. Run the following command:
   ```cmd
   streamlit run app.py
   ```

## Usage

Vidtranslate allows you to obtain video subtitles translated to English. You can then download both the translated English subtitles and the original subtitles.

## Troubleshooting

### Common Issues and Solutions

- **Installation Issues**: Ensure you are running Command Prompt or PowerShell as an Administrator.
- **ffmpeg Not Found**: Verify that ffmpeg was installed correctly by typing `ffmpeg -version` in Command Prompt.
- **Streamlit Not Found**: Ensure that Streamlit is installed by running `pip install streamlit`.
- **Model Performance**: The application uses OpenAI Whisper for obtaining transcripts. The default model is "medium" which requires ~5 GB of VRAM and has a relative speed of 2x. Depending on your system's specifications, you may need to adjust the model:

  - **tiny**: Requires ~1 GB VRAM, 32x speed
  - **base**: Requires ~1 GB VRAM, 16x speed
  - **small**: Requires ~2 GB VRAM, 6x speed
  - **medium**: Requires ~5 GB VRAM, 2x speed (default)
  - **large**: Requires ~10 GB VRAM, 1x speed

  Lower models will result in lower quality but faster processing times, and vice versa.

## Contributing

Currently, contributions are managed solely by the original author. You can view the project on GitHub: [GitHub Profile](https://github.com/AlgorithmicPV)

## Contact

For questions or support, please reach out through the GitHub repository.
