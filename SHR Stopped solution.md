It seems that the self-hosted runner stopped because it's designed to run in the foreground of the terminal when executed with `./run.sh`. This means that if you closed the terminal session or the EC2 instance restarted, the runner would have stopped. To ensure it runs persistently in the background and starts automatically, you should set it up as a service.

Here’s how to do that on your EC2 instance:

### 1. Navigate to the Runner Directory

First, make sure you’re in the `actions-runner` directory on your EC2 instance:

```bash
cd ~/actions-runner
```

### 2. Set Up the Runner as a Service

To run the self-hosted GitHub runner as a background service, GitHub provides a built-in script to install it as a service.

Run the following command in the `actions-runner` directory:

```bash
sudo ./svc.sh install
```

This command will install the runner as a service, making it easier to start, stop, or restart it.

### 3. Start the Service

After installing the service, start it using the following command:

```bash
sudo ./svc.sh start
```

### 4. Check the Status

You can check the status of the runner service to ensure it’s running:

```bash
sudo ./svc.sh status
```

### 5. Enable the Service to Start on Boot (Optional)

To ensure that the runner service starts automatically when the EC2 instance reboots, you can use the following command:

```bash
sudo systemctl enable actions.runner.<your-runner-name>.service
```

### Additional Notes

- **Replace `<your-runner-name>`**: When checking the status or enabling the service, replace `<your-runner-name>` with the specific name of your runner service. You can find the name of the service by running `systemctl list-units | grep actions.runner`.

- **Re-register the Runner**: If you’re still experiencing issues, there may have been an issue during setup. You might need to re-register the runner. To do this, stop the service, remove the runner, and start the configuration process again with a new registration token from your GitHub repository's settings.

### Example Commands

```bash
# Stop and remove the service (if needed)
sudo ./svc.sh stop
sudo ./svc.sh uninstall

# Re-configure the runner
./config.sh --url https://github.com/ashpaqueshaikh4236/machine-learning-project-with-mlflow --token <NEW_TOKEN>

# Re-install and start the service
sudo ./svc.sh install
sudo ./svc.sh start
```

After following these steps, the runner should be persistently running as a background service on your EC2 instance and ready to accept jobs.
