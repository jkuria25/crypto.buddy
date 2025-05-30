

crypto_data = {
    'Bitcoin': {
        'price_trend': 'upward',
        'energy_efficiency': 'low',
        'project_viability': 'high'
    },
    'Ethereum': {
        'price_trend': 'stable',
        'energy_efficiency': 'medium',
        'project_viability': 'high'
    },
    'Cardano': {
        'price_trend': 'upward',
        'energy_efficiency': 'high',
        'project_viability': 'medium'
    },
    'Dogecoin': {
        'price_trend': 'downward',
        'energy_efficiency': 'high',
        'project_viability': 'low'
    },
    'Polkadot': {
        'price_trend': 'stable',
        'energy_efficiency': 'medium',
        'project_viability': 'medium'
    }
}

def analyze_crypto(name):
    name = name.capitalize()
    if name not in crypto_data:
        return f"Sorry, I don't have data on {name}. Please ask about Bitcoin, Ethereum, Cardano, Dogecoin, or Polkadot."
    
    data = crypto_data[name]
    
    advice = f"Analysis for {name}:\n"
    
    if data['price_trend'] == 'upward':
        advice += "- The price trend is upward, indicating potential profitability.\n"
    elif data['price_trend'] == 'stable':
        advice += "- The price trend is stable, indicating moderate profitability.\n"
    else:
        advice += "- The price trend is downward, indicating potential risk.\n"
    
    if data['energy_efficiency'] == 'high':
        advice += "- The project has high energy efficiency, which is good for sustainability.\n"
    elif data['energy_efficiency'] == 'medium':
        advice += "- The project's energy efficiency is moderate.\n"
    else:
        advice += "- The project has low energy efficiency, which may raise sustainability concerns.\n"
    
  
    if data['project_viability'] == 'high':
        advice += "- The project shows high viability and strong fundamentals.\n"
    elif data['project_viability'] == 'medium':
        advice += "- The project has medium viability; monitor developments closely.\n"
    else:
        advice += "- The project viability is low, so be cautious with investments.\n"
    
   
    if data['price_trend'] == 'upward' and data['energy_efficiency'] in ['high', 'medium'] and data['project_viability'] in ['medium', 'high']:
        advice += "\nOverall, this looks like a promising investment opportunity! 🚀"
    elif data['price_trend'] == 'downward' or data['project_viability'] == 'low':
        advice += "\nBe careful! This investment carries higher risks. ⚠️"
    else:
        advice += "\nThis investment appears moderate; consider your risk tolerance before proceeding."
    
    return advice

def chatbot():
    print("Welcome to Your First AI-Powered Financial Sidekick! 🌟")
    print("Ask me about Bitcoin, Ethereum, Cardano, Dogecoin, or Polkadot.")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("\nWhich cryptocurrency do you want advice on? ").strip()
        
        if user_input.lower() == 'exit':
            print("Thanks for chatting! Stay crypto-savvy! ✨")
            break
        
        response = analyze_crypto(user_input)
        print("\n" + response)

if __name__ == "__main__":
    chatbot()

