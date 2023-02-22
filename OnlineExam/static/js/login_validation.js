function validate(){
    result=true
    username=document.getElementById('username')
    password=document.getElementById('password')
    if(username.value.length==0)
    {
      error1=document.getElementById('error1')
      error1.innerHTML='enter username'
      error1.style.margin='0px';  
      result=false
    }    
    else{
        error1=document.getElementById('error1')
        error1.innerHTML=''
        error1.style.margin='5px';  
    }
    if(password.value.length==0)
    {
    error2=document.getElementById('error2')
    error2.innerHTML='enter password'
    error2.style.margin='0px';  
    result=false
    }    
    else{
        error2=document.getElementById('error1')
        error2.innerHTML=''
        error2.style.margin='5px';  
    }
    return result
}