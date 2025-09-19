# AIMonks_Task

## How to Run the Application

To get the object detection application up and running, follow these steps:

1.  **Install Python:** If you don't have Python installed, download and install it from [python.org](https://www.python.org/downloads/). It's recommended to use Python 3.8 or newer.

2.  **Install Dependencies:** Navigate to the project directory in your terminal or command prompt and install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application:** Start the Flask development server by running:
    ```bash
    python app.py
    ```
    The application will typically run on `http://127.0.0.1:5000/` (or a similar local address).

4.  **Access the Web Interface:** Open your web browser and go to the address provided in the terminal output (e.g., `http://127.0.0.1:5000/`). You can then upload images for object detection through the web interface.

## How to Use the Web Interface

Once the application is running and you've accessed it in your browser:

1.  **Upload an Image:** Click on the "Choose File" button to select an image from your local machine.
2.  **Detect Objects:** Click the "Detect Objects" button. The application will process the image.
3.  **View Results:** After processing, the output images with detected objects will be displayed on the page.
4.  **Export JSON:** Click on the "JSONrt json" button if you want the output JSON.

## Output Location

The final outputs, including the images with detected objects and the corresponding JSON files with detection results, will be stored in the `static/outputs` directory within your project folder.

## How to Run with Docker

Alternatively, you can run the application using Docker:

1.  **Build the Docker Image:** Navigate to the project directory and build the Docker image:
    ```bash
    docker build -t aimonks-task .
    ```

2.  **Run the Docker Container:** Once the image is built, you can run the container, mapping port 5000 from the container to your host machine:
    ```bash
    docker run -p 5000:5000 aimonks-task
    ```

3.  **Access the Web Interface:** Open your web browser and go to `http://localhost:5000/` to access the application.