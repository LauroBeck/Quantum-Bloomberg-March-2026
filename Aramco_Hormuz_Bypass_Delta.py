import pandas as pd

def calculate_bypass_alpha(current_target, bypass_efficiency_gain):
    # Analyzing the Aramco Red Sea pivot impact
    final_target = current_target * (1 + (bypass_efficiency_gain / 100))
    alpha_gain = final_target - current_target
    
    report = {
        "Base_Target": current_target,
        "Red_Sea_Bypass_Gain": f"+{bypass_efficiency_gain}%",
        "Final_Risk_Adjusted_Target": round(final_target, 2),
        "Strategic_Delta": round(alpha_gain, 2)
    }
    return report

if __name__ == "__main__":
    # Target from your successful CVX Insurance Pivot run
    base_target = 194.01
    # Simulating a conservative 1.5% gain from restored Aramco supply chains
    efficiency_gain = 1.5 
    
    bypass_report = calculate_bypass_alpha(base_target, efficiency_gain)
    
    print("--- ARAMCO RED SEA BYPASS: TARGET ADJUSTMENT ---")
    for key, value in bypass_report.items():
        print(f"{key}: {value}")
