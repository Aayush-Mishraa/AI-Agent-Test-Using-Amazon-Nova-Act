"""
HTML Test Result Logger for Nova Act Test Scenarios
Generates comprehensive HTML reports with test execution details
"""

import os
import time
from datetime import datetime
from typing import List, Dict, Any
import json


class TestResultLogger:
    """Generates HTML reports for Nova Act test scenarios"""
    
    def __init__(self, scenario_name: str):
        self.scenario_name = scenario_name
        self.start_time = datetime.now()
        self.test_steps: List[Dict[str, Any]] = []
        self.results_dir = "results"
        self.current_step = 0
        self.passed_steps = 0
        self.failed_steps = 0
        
        # Create results directory if it doesn't exist
        os.makedirs(self.results_dir, exist_ok=True)
    
    def log_step(self, action: str, status: str = "passed", details: str = "", response: str = ""):
        """Log a test step with action, status, and details"""
        self.current_step += 1
        
        step_data = {
            "step_number": self.current_step,
            "action": action,
            "status": status.lower(),
            "details": details,
            "response": response,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }
        
        self.test_steps.append(step_data)
        
        if status.lower() == "passed":
            self.passed_steps += 1
        elif status.lower() == "failed":
            self.failed_steps += 1
        
        # Print to console
        status_icon = "✓" if status.lower() == "passed" else "✗"
        print(f"  {status_icon} Step {self.current_step}: {action} - {status.upper()}")
        if response:
            print(f"    Response: {response[:100]}...")
    
    def log_info(self, message: str):
        """Log informational message"""
        print(f"ℹ {message}")
    
    def log_error(self, error: str):
        """Log error message"""
        self.log_step("Error", "failed", error)
    
    def generate_html_report(self, save_path: str = None) -> str:
        """Generate comprehensive HTML report"""
        end_time = datetime.now()
        duration = (end_time - self.start_time).total_seconds()
        
        if save_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            save_path = os.path.join(self.results_dir, f"{self.scenario_name}_{timestamp}.html")
        
        total_steps = len(self.test_steps)
        pass_rate = (self.passed_steps / total_steps * 100) if total_steps > 0 else 0
        
        # Generate HTML content
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.scenario_name} - Test Report</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            min-height: 100vh;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2em;
            margin-bottom: 10px;
        }}
        
        .header .subtitle {{
            font-size: 1.1em;
            opacity: 0.9;
        }}
        
        .summary {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 30px;
            background: #f8f9fa;
        }}
        
        .summary-card {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-align: center;
        }}
        
        .summary-card .label {{
            font-size: 0.9em;
            color: #666;
            margin-bottom: 8px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        .summary-card .value {{
            font-size: 2em;
            font-weight: bold;
            color: #333;
        }}
        
        .summary-card.passed .value {{
            color: #28a745;
        }}
        
        .summary-card.failed .value {{
            color: #dc3545;
        }}
        
        .summary-card.rate .value {{
            color: #667eea;
        }}
        
        .progress-bar {{
            width: 100%;
            height: 30px;
            background: #e9ecef;
            border-radius: 15px;
            overflow: hidden;
            margin: 20px 0;
        }}
        
        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #28a745 0%, #20c997 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
            transition: width 0.3s ease;
        }}
        
        .test-steps {{
            padding: 30px;
        }}
        
        .test-steps h2 {{
            font-size: 1.5em;
            margin-bottom: 20px;
            color: #333;
        }}
        
        .step {{
            background: white;
            border: 1px solid #e1e4e8;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 15px;
            transition: box-shadow 0.2s ease;
        }}
        
        .step:hover {{
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }}
        
        .step-header {{
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 10px;
        }}
        
        .step-number {{
            background: #667eea;
            color: white;
            width: 35px;
            height: 35px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            flex-shrink: 0;
        }}
        
        .step-action {{
            flex: 1;
            font-size: 1.1em;
            color: #333;
            font-weight: 500;
        }}
        
        .step-status {{
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 0.85em;
            font-weight: bold;
            text-transform: uppercase;
        }}
        
        .step-status.passed {{
            background: #d4edda;
            color: #155724;
        }}
        
        .step-status.failed {{
            background: #f8d7da;
            color: #721c24;
        }}
        
        .step-status.skipped {{
            background: #fff3cd;
            color: #856404;
        }}
        
        .step-timestamp {{
            color: #666;
            font-size: 0.9em;
        }}
        
        .step-details {{
            margin-top: 10px;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 6px;
            color: #555;
            line-height: 1.6;
        }}
        
        .step-response {{
            margin-top: 10px;
            padding: 15px;
            background: #e7f3ff;
            border-left: 4px solid #2196F3;
            border-radius: 4px;
            color: #333;
            line-height: 1.6;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
            white-space: pre-wrap;
            word-break: break-word;
        }}
        
        .footer {{
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #666;
            border-top: 1px solid #e1e4e8;
        }}
        
        .metadata {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
            margin-top: 15px;
        }}
        
        .metadata-item {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        
        .metadata-label {{
            font-weight: bold;
            color: #333;
        }}
        
        @media print {{
            body {{
                background: white;
                padding: 0;
            }}
            
            .container {{
                box-shadow: none;
            }}
            
            .step:hover {{
                box-shadow: none;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🤖 Nova Act Test Report</h1>
            <div class="subtitle">{self.scenario_name}</div>
        </div>
        
        <div class="summary">
            <div class="summary-card">
                <div class="label">Total Steps</div>
                <div class="value">{total_steps}</div>
            </div>
            <div class="summary-card passed">
                <div class="label">Passed</div>
                <div class="value">{self.passed_steps}</div>
            </div>
            <div class="summary-card failed">
                <div class="label">Failed</div>
                <div class="value">{self.failed_steps}</div>
            </div>
            <div class="summary-card rate">
                <div class="label">Pass Rate</div>
                <div class="value">{pass_rate:.1f}%</div>
            </div>
            <div class="summary-card">
                <div class="label">Duration</div>
                <div class="value">{duration:.1f}s</div>
            </div>
        </div>
        
        <div style="padding: 0 30px;">
            <div class="progress-bar">
                <div class="progress-fill" style="width: {pass_rate}%">
                    {pass_rate:.1f}% Passed
                </div>
            </div>
        </div>
        
        <div class="test-steps">
            <h2>📋 Test Execution Steps</h2>
"""
        
        # Add test steps
        for step in self.test_steps:
            html_content += f"""
            <div class="step">
                <div class="step-header">
                    <div class="step-number">{step['step_number']}</div>
                    <div class="step-action">{step['action']}</div>
                    <div class="step-status {step['status']}">{step['status']}</div>
                    <div class="step-timestamp">⏱ {step['timestamp']}</div>
                </div>
"""
            
            if step['details']:
                html_content += f"""
                <div class="step-details">
                    <strong>Details:</strong> {step['details']}
                </div>
"""
            
            if step['response']:
                html_content += f"""
                <div class="step-response">
                    <strong>Response:</strong><br>
                    {step['response']}
                </div>
"""
            
            html_content += """
            </div>
"""
        
        # Add footer
        html_content += f"""
        </div>
        
        <div class="footer">
            <div class="metadata">
                <div class="metadata-item">
                    <span class="metadata-label">Start Time:</span>
                    <span>{self.start_time.strftime("%Y-%m-%d %H:%M:%S")}</span>
                </div>
                <div class="metadata-item">
                    <span class="metadata-label">End Time:</span>
                    <span>{end_time.strftime("%Y-%m-%d %H:%M:%S")}</span>
                </div>
                <div class="metadata-item">
                    <span class="metadata-label">Total Duration:</span>
                    <span>{duration:.2f} seconds</span>
                </div>
                <div class="metadata-item">
                    <span class="metadata-label">Report Generated:</span>
                    <span>{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</span>
                </div>
            </div>
            <p style="margin-top: 20px;">Generated by Nova Act Test Automation Framework</p>
        </div>
    </div>
</body>
</html>
"""
        
        # Save HTML report
        with open(save_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"\n{'='*60}")
        print(f"✅ HTML Report Generated: {save_path}")
        print(f"{'='*60}")
        
        return save_path
    
    def wrap_test(self, func):
        """Decorator to wrap test execution with automatic reporting"""
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                self.log_error(f"Test execution failed: {str(e)}")
                raise
            finally:
                self.generate_html_report()
        return wrapper
