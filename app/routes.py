from flask import render_template, request, redirect, url_for
from app import app

@app.route('/')
def home():
    return "Welcome to the Diary App"

# Add more routes as we progress
