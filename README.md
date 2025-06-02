# webhook-repo

This repository is part of the GitHub Webhook integration project.

- **action-repo**: Contains the GitHub repository that triggers webhook events on Push, Pull Request, and Merge.
- **webhook-repo**: Flask application that receives webhook events from GitHub, stores relevant data in MongoDB Atlas, and displays recent events on a UI.


Listens for GitHub events: push, pull_request (open), and pull_request (merge).
- Stores minimal necessary data in MongoDB.
- UI polls MongoDB every 15 seconds to display the latest events.
- Clean, minimal interface to show GitHub activity.

## Setup Instructions (For webhook-repo)
1. Clone the repo:

2. Create and activate a virtual environment (optional but recommended):


3. Install dependencies:



4. Create a `.env` file in the root directory and add your MongoDB connection string:



5. Run the Flask app:



6. Expose your local server to the internet using **ngrok** or a similar tool:


Use the generated URL as your GitHub webhook URL.

## How to Test
- Push commits to the **action-repo**.
- Create Pull Requests and Merge them.
- The webhook-repo will receive events and store them in MongoDB.
- Visit `http://localhost:5000/` to see the latest events in the UI.

## Important Notes
- Make sure your `.env` file is included in `.gitignore` to avoid pushing sensitive credentials.
- This project uses MongoDB Atlas as the database.

## Links
- Action Repo: [https://github.com/Vinaylakra/action-repo](https://github.com/Vinaylakra/action-repo)
- Webhook Repo: [https://github.com/Vinaylakra/webhook-repo](https://github.com/Vinaylakra/webhook-repo)

---

## How to Use `.gitignore`

1. Create a file named `.gitignore` in the root directory of your project (if it doesn't exist already).

2. Add the following line to it to ignore your environment variables file:

