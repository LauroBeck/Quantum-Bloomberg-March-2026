import pandas as pd

def analyze_vix_decay(current_vix, target_vix_floor):
    # Analyzing how fast 'Systemic Noise' must dissipate for Tech recovery
    decay_needed = current_vix - target_vix_floor
    decay_pct = (decay_needed / current_vix) * 100
    
    analysis = {
        "Current_VIX": current_vix,
        "Target_VIX": target_vix_floor,
        "Noise_Reduction_Required": f"{round(decay_pct, 2)}%",
        "Market_State": "High Decoherence" if current_vix > 20 else "Stable"
    }
    
    return analysis

if __name__ == "__main__":
    # Current VIX from March 4 Bloomberg screenshots
    current_vix = 23.57 
    # Historical baseline for "benign" war reaction
    baseline = 18.50 
    
    vix_report = analyze_vix_decay(current_vix, baseline)
    
    print("--- VIX DECOHERENCE (NOISE) REPORT ---")
    for key, value in vix_report.items():
        print(f"{key}: {value}")
        
    print(f"\n[STRATEGY] Nasdaq recovery requires a {vix_report['Noise_Reduction_Required']} drop in VIX.")
