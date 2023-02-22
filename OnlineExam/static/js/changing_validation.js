function changeValidate(){
    result=true
    objinput=document.getElementsByTagName('input')
    if(objinput[1].value.length==0)
    {
        error=document.getElementById('error1')
        error.innerHTML='enter usermane'
        error.style.margin='0px'
        result=false
    }
    else{
       error=document.getElementById('error1')
       error.innerHTML=''
       error.style.margin='15px'
    }
    if(objinput[2].value.length==0){
        error=document.getElementById('error2')
        error.innerHTML='enter new password'
        error.style.margin='0px'
        result=false
    }
    else{
        error=document.getElementById('error2')
        error.innerHTML=''
        error.style.margin='15px' 
    }
    if(objinput[3].value.length==0){
        error=document.getElementById('error3')
        error.innerHTML='confirm password'
        error.style.margin='0px'
        result=false
    }
    else{
        error=document.getElementById('error3')
        error.innerHTML='' 
        error.style.margin='15px'


    }
   return result
}