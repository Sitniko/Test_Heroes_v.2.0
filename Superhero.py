import Imports

def func_for_heroes(lo_flag, lo_sex):
    response = Imports.requests.get('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json')
    big_json_data = response.json() 
    
    lo_max_height = 0
    lo_tallest_character = None
    
    lo_rezult_list = []
    for character in big_json_data:
        try:
          
            lo_occupation = str(character['work']['occupation'])
            lo_gender = str(character['appearance']['gender'])
            
            if (lo_occupation != "-") == lo_flag and lo_gender == lo_sex:
                lo_rezult_list.append(character)
                
                
                lo_height_str = character['appearance']['height'][1]
                lo_height_cm = int(lo_height_str.split()[0])
            
                
                if lo_height_cm > lo_max_height:
                    lo_max_height = lo_height_cm
                    lo_tallest_character = character
            lo_Final_person_name = lo_tallest_character['name']
                     
        except:
            
            continue
    
    
    return lo_Final_person_name

def get_user_info():
    while True:
        try:
            lo_work_input = input("Наличие работы (да/нет): ").strip()
            if lo_work_input == 'да':
                lo_has_work = True
            elif lo_work_input == 'нет':
                lo_has_work = False
            else:
                print("Пожалуйста, введите 'да' или 'нет'")
                continue
        
            lo_gender_input = input("Введите пол (м/ж или '-'): ").strip()
            if lo_gender_input == 'м':
                lo_gender = 'Male'
            elif lo_gender_input == 'ж':
                lo_gender = 'Female'
            elif lo_gender_input == '-':
                lo_gender = '-'
            else:
                print("Пожалуйста, введите 'м' или 'ж' или '-'")
                continue
            
            return lo_has_work, lo_gender
            
        except KeyboardInterrupt:
            print("\nПрерывание")
            return None, None


if __name__ == "__main__":
    gl_work_status, gl_gender_info = get_user_info()
    print(func_for_heroes(gl_work_status, gl_gender_info))            