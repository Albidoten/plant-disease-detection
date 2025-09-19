# 🔍 YOLO Object Detection Web Application

A modern, responsive web application that uses YOLOv8 for real-time object detection. Upload images and get instant AI-powered object detection with bounding boxes and confidence scores.

## ✨ Features

- 🖼️ **Drag & Drop Upload**: Modern file upload interface
- 🔍 **YOLOv8 Detection**: State-of-the-art object detection
- 📊 **Visual Results**: Bounding boxes and confidence scores
- 🎨 **Modern UI**: Beautiful, responsive design
- ⚡ **Fast Processing**: Efficient image processing
- 📱 **Mobile Friendly**: Works on all devices

## 🚀 Live Demo

[**Try it live here!**](https://your-app-url.onrender.com) *(Replace with your deployed URL)*

## 🛠️ Installation

### Local Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/yolo-object-detection.git
   cd yolo-object-detection
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open your browser** and go to `http://localhost:5000`

## 🌐 Deploy to Cloud

### Quick Deploy to Render (Free)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

1. Fork this repository
2. Sign up at [render.com](https://render.com)
3. Create new Web Service from your GitHub repo
4. Use these settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
5. Deploy!

### Alternative Platforms

- **Railway**: [railway.app](https://railway.app) - Auto-detects Python
- **PythonAnywhere**: [pythonanywhere.com](https://pythonanywhere.com) - Free tier available
- **Heroku**: [heroku.com](https://heroku.com) - Paid plans

## 📖 Usage

1. **Upload Image**: Drag & drop or click to select an image
2. **Wait for Processing**: YOLOv8 analyzes your image
3. **View Results**: See detected objects with bounding boxes
4. **Check Details**: Review confidence scores and object classes

## 🎯 Supported Objects

The YOLOv8 model can detect 80 different object classes including:
- **People & Animals**: person, cat, dog, horse, etc.
- **Vehicles**: car, truck, bus, motorcycle, bicycle, etc.
- **Objects**: chair, table, laptop, phone, book, etc.
- **Food**: apple, banana, pizza, cake, etc.
- **And many more!**

## 🔧 Technical Details

- **Backend**: Flask (Python)
- **AI Model**: YOLOv8n (Ultralytics)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Image Processing**: OpenCV, Pillow
- **Deployment**: Docker-ready, cloud-compatible

## 📁 Project Structure

```
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Frontend template
├── Procfile           # Deployment configuration
├── runtime.txt        # Python version specification
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## ⚙️ Configuration

- **Max File Size**: 16MB
- **Supported Formats**: PNG, JPG, JPEG, GIF, BMP, WebP
- **Model**: YOLOv8n (optimized for speed)
- **Port**: Configurable via environment variable

## 🚨 Troubleshooting

### Common Issues

1. **Model Download**: First run downloads YOLOv8 model (~6MB)
2. **Memory Limits**: Free hosting has memory constraints
3. **Cold Starts**: Apps may sleep when inactive
4. **Processing Time**: Large images take longer to process

### Solutions

- Use smaller images for faster processing
- Consider paid hosting for heavy usage
- Optimize images before upload
- Check platform logs for specific errors

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [Ultralytics](https://ultralytics.com/) for YOLOv8
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Bootstrap](https://getbootstrap.com/) for the UI components

---

**Made with ❤️ and AI** | [Report Issues](https://github.com/YOUR_USERNAME/yolo-object-detection/issues) | [Request Features](https://github.com/YOUR_USERNAME/yolo-object-detection/issues/new)
