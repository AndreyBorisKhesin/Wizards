# TextMD

## Introduction
TextMD is an interactive server accessible through SMS that can diagnose a
patient's condition in real time and direct a patient to an emergency service if needed.
It can be used to help improve dissemination of health care knowledge of
third world countries, such as Bangladesh.

## How It Works

TextMD uses _Twilio_ as a relay to send text messages.
It runs a local server using _Flask_ that is tunneled to public access using _ngrok_.
TextMD uses the _infermedica_ API to diagnose the possible conditions afflicting the user based on their stated symptoms, gender, and age.
If the user requests immediate help, TextMD directs a patient to a local
emergency service telephone number.

TextMD also storers the diagnosed diseases matched to their geographical location for later use by government agencies.
