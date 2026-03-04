import pandas as pd

def run_macro_simulation():
    # Data from March 4, 2026: The "Hormuz Insurance" Pivot
    # Reflecting the KOSPI -8.10% crash and the Nasdaq Fut recovery
    data = {
        "Asset": ["Chevron (Anchor)", "Nasdaq Fut", "KOSPI (Circuit)", "DAX", "VIX"],
        "Current_Pct": [1.52, 0.03, -8.10, -3.44, 9.93], 
        "BNY_Resilience": [10.1, 10.1, 10.1, 10.1, 0.0]
    }

    df = pd.DataFrame(data)

    # Calculate Survival Metrics
    # Alpha Gap: Chevron vs the worst hit Asian index
    alpha_gap = df.loc[0, 'Current_Pct'] - df.loc[2, 'Current_Pct']
    
    # Insurance Impact Score: Simulating a 2% recovery if USIDFC plan succeeds
    df['Recovery_Potential'] = df['Current_Pct'] + 2.0 

    print("--- MARCH 4, 2026: GLOBAL RECOVERY STATUS ---")
    print(df.to_string(index=False))
    print(f"\n[SIGNAL] SURVIVAL ALPHA: +{alpha_gap:.2f}%")
    print(f"[CATALYST] USIDFC Insurance is currently de-risking the 'Hormuz Standstill'.")
    
    return df

if __name__ == "__main__":
    simulation_results = run_macro_simulation()
