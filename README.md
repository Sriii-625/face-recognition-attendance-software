# face-recognition-attendance-software
Employee Face Recognition Attendance System


This repository contains a Python-based Employee Attendance Management System that uses Face Recognition for automated attendance tracking. The system is built using Tkinter for the GUI, OpenCV for face detection and recognition, and MySQL for data storage.

# Project Overview

The system consists of three core modules:

Generator – Captures employee photo samples using a webcam.

Trainer – Trains a face recognition model using OpenCV.

Detector – Identifies employees, records attendance, and exports data.



# Features

 # Secure Login System
Employee authentication with username and password stored in MySQL.

Includes a "Forgot Password" feature.

Access restricted to authorized personnel only.



 # Attendance System Interface
The user-friendly Tkinter interface provides quick access to key features:

Employee Details – Manage employee records.

Face Recognition – Detects and identifies employees in real time.

Attendance System – Displays and exports attendance logs.

Train Data – Initiates the training process for new employees.

Developer Info – Displays system details.

Exit – Secure logout option.



 # Employee Management
Stores employee details including ID, role, department, name, email, and phone number in a MySQL database.

Captures 100 face samples per employee for training using OpenCV.



 # Face Detection & Recognition
Uses Haar Cascade Classifier for face detection.

Implements the LBPH (Local Binary Patterns Histograms) algorithm for accurate recognition.

The Face Recognition module automatically marks attendance.



 # Attendance & Data Export
Attendance records include timestamps and dates.

Data can be exported to CSV files.

Supports data updates and re-imports for maintaining records.



 # Database Integration
MySQL database stores employee records and attendance logs.

Functions implemented to insert, fetch, update, and reset data efficiently.



 # GUI Enhancements
Real-time clock integrated into the interface.

Help and developer info sections for ease of use.

Exit confirmation to prevent accidental closure.



This system provides an automated, secure, and efficient way to manage employee attendance using face recognition. 
