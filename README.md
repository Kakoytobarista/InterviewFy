# InterviewFy

InterviewFy is a service designed to help you prepare for interviews by allowing you to create and manage interview sessions and tasks. After completing an interview, you'll receive information about the session and your performance via a chat bot.

___
## Miro Schema:
`https://miro.com/app/board/uXjVNlnaud8=/?share_link_id=707588856328`
___
## Features

- **Create Interviews:** Easily create interview sessions with customizable tasks.
- **Track Progress:** Monitor your performance and progress through interview sessions.
- **Chat Bot Integration:** Receive interview session details and feedback directly in your chat application.

___
## Environment Variables

To use InterviewFy, you'll need to set up the following environment variables in a `.env` file:

- `DB_ECHO`: Set to `True` to enable SQLAlchemy echo mode for debugging.
- `PROJECT_NAME`: Name of the InterviewFy project.
- `VERSION`: Version of the InterviewFy project.
- `DEBUG`: Set to `True` to enable debugging mode.
- `CORS_ALLOWED_ORIGINS`: Origins allowed for CORS requests.
- `POSTGRES_USER`: PostgreSQL username.
- `POSTGRES_PASSWORD`: PostgreSQL password.
- `POSTGRES_HOST`: PostgreSQL host.
- `POSTGRES_PORT`: PostgreSQL port.
- `POSTGRES_DB`: PostgreSQL database name.
- `TELEGRAM_TOKEN`: Token for accessing the Telegram API.
- `CHAT_ID`: ID of the chat where interview session information will be sent.

___
## Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/interviewfy.git
    cd interviewfy
    ```

2. Create a `.env` file and populate it with the required environment variables.

3. Build and start the InterviewFy service:

    ```bash
    docker-compose up --build
    ```

4. Once the service is running, you can access InterviewFy at `http://localhost:8000` (API), UI: `http://localhost:3000` 

## Contributing

Contributions are welcome! If you have any ideas for improvements or find any issues, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
