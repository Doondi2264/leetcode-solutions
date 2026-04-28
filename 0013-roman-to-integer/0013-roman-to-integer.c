int value(char t);
int romanToInt(char* s) {
    int r = 0;
    int l = strlen(s);
    for (int i=0;i<l;i++){
        int a = value(s[i]);
        if ((i+1) < l){
            int b = value(s[i+1]);
            if (a>=b){
                r +=a;
            }
            else{
                r+=(b-a);
                i++;
            }
        }
        else{
            r+=a;
        }
    }
    return r;
}

int value(char d){
    switch (d){
        case 'I':
        return 1;

        case 'V':
        return 5;

        case 'X':
        return 10;

        case 'L':
        return 50;

        case 'C':
        return 100;

        case 'D':
        return 500;

        case 'M':
        return 1000;

        default:
        return-1;
        
    }
}