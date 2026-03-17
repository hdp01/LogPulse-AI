# 🛠️ Setup & Execution Guide

## 1. Run the Pipeline

The master script handles environment setup, log generation, and AI analysis in one go.

# Step 1: Give execution permissions to the script
chmod +x run_project.sh

# Step 2: Execute the pipeline
./run_project.sh

## 2. Configure the Kibana Dashboard

Once the script outputs **"AI Analysis Complete"**, follow these steps:

### Access Kibana
Open your browser and go to:  
http://localhost:5601

### Create Data View

- Navigate to:  
  `Management → Stack Management → Data Views`

- Click **Create data view**

- Fill in:
  - **Name:** Web Logs Analysis  
  - **Index Pattern:** web-logs  
  - **Timestamp field:** Select *"I don't want to use the time filter"*

- Click **Save data view to Kibana**

## 3. Visualize the AI Output

### Open Discover
Navigate to:  
`Analytics → Discover`

### Select View
Ensure **Web Logs Analysis** is selected in the dropdown.

### Create Chart

- In the left field list, find **`is_anomaly`**
- Click **is_anomaly** and select **Visualize**

### Configure Chart

- On the right configuration panel, drag **`is_anomaly`** to the **Horizontal Axis**
- Under **Vertical Axis**:
  - Click the current function (e.g., Median)
  - Change it to **Count**

## 4. Final Output Verification

Your chart should now display two distinct bars:

- **Bar 0 (Normal):**  
  Contains your `/home` requests with low latency.

- **Bar 1 (Anomaly):**  
  Contains your `/login` requests which the AI flagged due to high latency and specific log keywords.

## 5. Cleanup

To stop the infrastructure and free up system memory:

docker compose down