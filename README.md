# my_download

Executa a Aplicação GUI principal 

```bash
python3 main.py
```

## Telas

Principal 

![Tela Principal](https://github.com/armandossrecife/my_download/blob/main/docs/tela_principal.png)

Executa Download 

![Executa Download](https://github.com/armandossrecife/my_download/blob/main/docs/executa_download.png)

# Explaining the code

Here's a breakdown of the code and its functionality:

## 1. Imports:

**requests**: For downloading files.

**tqdm**: For creating a progress bar in the console.

**tkinter**: For creating the GUI elements.

**urllib.parse**: For parsing URLs.

**os**: For file path operations.

## 2. Classes:

**Util**:

extrair_nome_extensao_url: Extracts the filename and extension from a URL.

**Download**:

Handles file downloads with progress updates.

Uses requests to download the file in chunks.

Provides a set_callback method to set a callback function for progress updates.

Calls the callback during the download with the total size and current progress.

**MyWindow**:

Creates the Tkinter GUI.

Has an entry for the URL, a label to show progress, a progress bar, and a download button.

download_with_progress_bar: Initiates the download with a callback to update the progress bar.

## main script:

Creates a MyWindow instance.

Starts the Tkinter main loop.

## 3. User Interaction:

Enter a URL in the entry field.

Click the "Download" button.

Observe the progress bar and label updating as the download progresses.

# Key Points:

**Callbacks**: The Download class efficiently communicates progress updates using a callback mechanism.

**GUI Integration**: The MyWindow class effectively integrates the download functionality with a user-friendly Tkinter interface.

**Clear Structure**: The code is well-organized and easy to understand due to class separation and modularity.

**Informative Progress**: The progress bar and label provide clear visual feedback during the download process.

**Error Handling**: The Download class includes basic error handling for invalid URLs and connection issues.

# Install dependencies

```bash
pip install requests
pip install tqdm
pip install requests-mock
```

# Perform automatic tests

## Run your tests with unittest

```bash
python3 -m unittest test_util test_download
```

## Run your tests with Coverage
  
```bash
coverage run -m unittest test_util.py test_download.py
```

## Generate an HTML report related to coverage tests:

```bash
coverage html
```