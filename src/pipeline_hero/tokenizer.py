from pathlib import Path
from typing import List
import json


class CodeWiseTokenizer:
    """Tokenizer for medical codes using WordLevel vocabulary mapping"""
    
    def __init__(self, path_tokenizer:str = None, vocab: List[str] = None, special_tokens: List[str] = None):
        """Initialize tokenizer"""

        if path_tokenizer:
            with open(path_tokenizer, "r") as f:
                self.token_to_id = json.load(f)
        else:
            self.vocab = vocab
            self.special_tokens = special_tokens or []
            self.token_to_id = {}

            self.build_from_list()
        self.id_to_token = {v: k for k, v in self.token_to_id.items()}
    
    def build_from_list(self):
        """Build tokenizer from list of medical codes
        
        Args:
            tokens: List of tokens (includes special tokens and medical codes)
        """
        # Create vocab with token IDs
        tokens = self.special_tokens + self.vocab
        self.token_to_id = {token: idx for idx, token in enumerate(tokens)}
        print(f"[Tokenizer] Built vocabulary with {len(self.token_to_id)} tokens")
    
    def encode(self, codes: List[str]) -> List[int]:
        """Convert list of medical codes to token IDs
        
        Args:
            codes: List of medical codes
            
        Returns:
            List of token IDs
        """
        return [self.get_token_id(code) for code in codes]
    
    def decode(self, ids: List[int]) -> List[str]:
        """Convert token IDs back to text
        
        Args:
            ids: List of token IDs
            
        Returns:
            List of token strings
        """
        return [self.id_to_token.get(token_id, "[UNK]") for token_id in ids]
    

    
    def get_vocab_size(self) -> int:
        """Get vocabulary size
        
        Returns:
            Number of tokens in vocabulary
        """
        return len(self.token_to_id)
    
    def get_token_id(self, token: str) -> int:
        """Get token ID for a given token
        
        Args:
            token: Token string
            
        Returns:
            Token ID
        """
        return self.token_to_id.get(token, self.token_to_id.get("[UNK]", 1))
    
    def get_token(self, token_id: int) -> str:
        """Get token string for a given token ID
        
        Args:
            token_id: Token ID
            
        Returns:
            Token string
        """
        
        return self.id_to_token.get(token_id, "[UNK]")

    def save_tokenizer(self, output_path: str):
        """Save tokenizer to disk
        
        Args:
            output_path: path to save the tokenizer file
        """
        # Save tokenizer as JSON        import json
        with open(output_path, "w") as f:
            json.dump(self.token_to_id, f)

    