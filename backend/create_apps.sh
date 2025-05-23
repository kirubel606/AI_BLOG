#!/bin/bash

# List of app names
apps=("settings" "resource" "collaborations" "contact_us" "faq" "rnd" "about_us" "news" "categories" "events" "quotes")

# Create each app and add necessary files
for app in "${apps[@]}"; do
    echo "Creating app: $app"
    python3 manage.py startapp $app
    
    if [ -d "$app" ]; then
        touch $app/serializers.py
        touch $app/urls.py
        echo "App '$app' created with serializers.py and urls.py."
    else
        echo "Failed to create app '$app'."
    fi
done
