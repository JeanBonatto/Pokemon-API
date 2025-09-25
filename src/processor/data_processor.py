class DataProcessorString:
    @staticmethod
    def process_string(value: str) -> str:
         # Convert to string if it's an integer
        if isinstance(value, int):
            return str(value)
            
        # Process string
        if isinstance(value, str):
            return value.lower().strip()
            
        # For any other type, convert to string
        return str(value)