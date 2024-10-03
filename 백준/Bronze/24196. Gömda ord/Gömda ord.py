def decrypt_message(encrypted):
    decrypted = []
    index = 0
    
    while index < len(encrypted):
        decrypted.append(encrypted[index])
        
        if index < len(encrypted) - 1: 
            step = ord(encrypted[index]) - ord('A') + 1 
            index += step
        else:
            break
    
    return ''.join(decrypted)

encrypted_input = input().strip()
print(decrypt_message(encrypted_input))
