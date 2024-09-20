#Programmed by Arrtix_x

import random

running = True
while running:
    try:
        length = int(input("Length: "))
        
        charmap = "0;1;2;3;4;5;6;7;8;9;a;b;c;d;e;f;g;h;i;j;k;l;m;n;o;p;q;r;s;t;u;v;w;x;y;z;A;B;C;D;E;F;G;H;I;J;K;L;M;N;O;P;Q;R;S;T;U;V;W;Y;Z;!;@;#;?;/;*;-;+;="
        splitCharMap = charmap.strip().split(";")
        
        password = ""
        
        for i in range(length):
            randomChoice = int(random.randint(0, 60))
            password = str(password) + str(splitCharMap[randomChoice - 1])
            
        print(f"Final password: {password}")
        
    except ValueError:
        print("Error: Option 'length' is not numeric!")
