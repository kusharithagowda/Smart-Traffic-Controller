Automatic Traffic Controller using IoT and Machine Learning:

A smart traffic control system that uses IoT sensors and machine learning to dynamically manage traffic signals based on real-time conditions like vehicle count and weather.
![image](https://github.com/user-attachments/assets/11213629-3c2f-4557-9fb7-67bc00a0e638)

Features

Real-time traffic data collection using IoT

ML-based signal time optimization

Weather-based signal adjustment

Vehicle detection and counting

Data visualization (using Matplotlib or similar)

📁 Project Structure

|-------------|-------------|
| `pcl1.py`   | Plots relationship between traffic density and green light duration |
| `pcl2.py`   | Shows accuracy of the ML model over training iterations |
| `pcl3.py`   | Visualizes vehicle count across lanes |
| `pcl4.py`   | Adjusts green light timing based on weather conditions |
| `pcl5.py`   | Trains and visualizes a multi-class SVM for traffic classification |
| `pcl6.py`   | Full simulation: generates synthetic data, trains SVM, and simulates signal adjustment |

🎯 Features

- 🧠 Machine Learning (SVM) for traffic classification
- 📡 Simulated IoT sensor input (vehicle count, traffic density)
- 🌦️ Weather-aware signal timing
- 📊 Real-time visualizations using `matplotlib`
- 🔁 Multiple scenario simulations with live signal adjustment logic

🛠️ Technologies Used

- **Python**
- **scikit-learn** – For SVM model training and prediction
- **NumPy / Pandas** – Data handling and synthetic data generation
- **Matplotlib** – Visualization of traffic behavior and model performance

  
## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/smart-traffic-controller.git
cd smart-traffic-controller

Example Output (from pcl6.py)
Model Accuracy: 93.33%
Predicted Traffic Class: 2 (Vehicle Count: 95, Traffic Density: 7.43)
Traffic is heavy: Green light for 60 seconds.
![image](https://github.com/user-attachments/assets/3a58eeb9-ae04-4383-b0c4-bb945c8fc774)
![image](https://github.com/user-attachments/assets/b7bd64a3-eabe-4563-be91-ae7e12b30cca)
![image](https://github.com/user-attachments/assets/eed63031-1282-4f39-b162-5c509ca3aa57)
![image](https://github.com/user-attachments/assets/ad7b46df-6afd-4467-ad84-8612ea6618c3)
![image](https://github.com/user-attachments/assets/6eae9da0-f3a1-440e-abd2-48149540161f)


 How It Works
Synthetic traffic data is generated (vehicle count + density).

Data is labeled as light, moderate, or heavy traffic.

A Support Vector Machine (SVM) is trained to classify traffic levels.

Based on prediction, green light duration is dynamically set.

Additional plots help visualize traffic and system performance.

📊 Visuals
📈 Traffic Density vs. Green Light Duration

📉 Model Accuracy over Iterations

🛣️ Lane-wise Vehicle Distribution

🌧️ Weather vs. Signal Timing

🧭 SVM Decision Boundaries for Traffic Classes
👤 Author
Suviii
🔗 GitHub: kusharithagowda
📬 Email: kusharithagowda@gmail.com

