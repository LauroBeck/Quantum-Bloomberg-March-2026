import pandas as pd

def calculate_insurance_pivot(current_price, recovery_factor):
    # Analyzing the shift from "Prohibitive Risk" to "USIDFC Insured"
    projected_price = current_price * (1 + (recovery_factor / 100))
    delta = projected_price - current_price
    
    metrics = {
        "Status": "Hormuz De-risking",
        "Base_Price": current_price,
        "Insurance_Delta": round(delta, 2),
        "Projected_Target": round(projected_price, 2)
    }
    
    return metrics

if __name__ == "__main__":
    # Current CVX price from Bloomberg data
    cvx_price = 190.21 
    # Using your simulation's +2.0% insurance recovery boost
    boost = 2.0 
    
    result = calculate_insurance_pivot(cvx_price, boost)
    
    print("--- CHEVRON (CVX) INSURANCE PIVOT ANALYSIS ---")
    for key, value in result.items():
        print(f"{key}: {value}")
    
    print(f"\n[VERDICT] CVX target adjusted to ${result['Projected_Target']} on USIDFC news.")
