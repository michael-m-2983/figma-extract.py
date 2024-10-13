# figma-extract.py

`figma-extract.py` is a tool written in Python designed to quickly view and extract data from Figma `.fig` files.

## Requirements

* Python 3.X
* Pygame (If you want to use the GUI display)
* A `.fig` file

## Usage

1. Clone the GitHub repository

    ```sh
    git clone https://github.com/michael-m-2983/figma-extract.git
    cd figma-extract
    ```

2. Display the help menu

    ```sh
    python figma-extract.py --help
    ```

    This will display a menu with details on all of the available CLI options.

3. Execute the Python script

    ```sh
    # Extract the metadata only
    python figma-extract.py -m metadata.json file.fig

    # Extract the thumbnail only
    python figma-extract.py -t thumbnail.png file.fig

    # Extract everything from the graphic using the unzip tool.
    # This will create a new folder called 'graphic'.
    unzip file.fig -d graphic

    # Preview the graphic's thumbnail
    python figma-extract.py file.fig
    ```

## Contributions

Contributions are welcome. Feel free to fork the repository and make a pull request.
