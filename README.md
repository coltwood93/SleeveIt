# SleeveIt

SleeveIt is a web application that helps you decide whether to wear long or short sleeves based on the weather in a given city. It uses the OpenWeatherMap API to fetch weather data and provides a simple recommendation.

## About the Project

This project consists of three main components:

*   **Frontend (`sleeve-it`):** A Vue.js single-page application that provides the user interface.
*   **Backend (`server`):** A Flask API that fetches weather data from the OpenWeatherMap API and provides a sleeve recommendation.
*   **Microservice (`microservice`):** A small Flask service that provides random city data to the frontend.

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

*   Python 3.x
*   Node.js and npm

### Installation

1.  **Clone the repo**
    ```sh
    git clone https://github.com/your_username_/SleeveIt.git
    ```
2.  **Set up the backend**
    *   Navigate to the `server` directory:
        ```sh
        cd server
        ```
    *   Install the Python dependencies:
        ```sh
        pip install -r requirements.txt
        ```
3.  **Set up the frontend**
    *   Navigate to the `sleeve-it` directory:
        ```sh
        cd ../sleeve-it
        ```
    *   Install the npm packages:
        ```sh
        npm install
        ```

### Configuration

1.  **Create a `.env` file** in the `server` directory.
2.  **Add your OpenWeatherMap API key** to the `.env` file:
    ```
    API_KEY=your_api_key_here
    ```
3.  **(Optional)** You can also set the temperature threshold for the sleeve recommendation in the `.env` file. The default is 69°F.
    ```
    SLEEVE_THRESHOLD_F=72
    ```

### Running the Application

1.  **Start the microservice**
    *   In a terminal, navigate to the `microservice` directory and run:
        ```sh
        python micro_server.py
        ```
    *   The microservice will be running at `http://127.0.0.1:5001`.
2.  **Start the backend server**
    *   In a new terminal, navigate to the `server` directory and run:
        ```sh
        python app.py
        ```
    *   The backend server will be running at `http://127.0.0.1:5000`.
3.  **Start the frontend**
    *   In a new terminal, navigate to the `sleeve-it` directory and run:
        ```sh
        npm run dev
        ```
    *   The frontend development server will be running at `http://localhost:5173`.

You can now open your browser and navigate to `http://localhost:5173` to use the application.