#!/usr/bin/env python3
"""
Simple HTTP server for testing the JitoX V2 Mini-App locally
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers for testing
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def main():
    # Change to the directory containing the Mini-App files
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"🚀 JitoX V2 Mini-App Test Server")
        print(f"📱 Server running at: http://localhost:{PORT}")
        print(f"🌐 Open in browser: http://localhost:{PORT}/index.html")
        print(f"⏹️  Press Ctrl+C to stop the server")
        print("-" * 50)
        
        # Try to open browser automatically
        try:
            webbrowser.open(f'http://localhost:{PORT}/index.html')
            print("✅ Browser opened automatically")
        except:
            print("⚠️  Could not open browser automatically")
            print("   Please manually open: http://localhost:8000/index.html")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped")
            sys.exit(0)

if __name__ == "__main__":
    main()
