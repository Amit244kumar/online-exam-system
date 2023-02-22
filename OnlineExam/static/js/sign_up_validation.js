function validate(){
    result=true
    inputObj=document.getElementsByTagName('input')
    error1=document.getElementById('error1')
    error2=document.getElementById('error2')
    error3=document.getElementById('error3')
    if(inputObj[1].value.length==0)
    {
        error1.innerHTML='enter username'
        error1.style.margin='0px'
        result=false
    }
    else{
        error1.innerHTML=''
        error1.style.margin='5px'
    }
    if(inputObj[2].value.length==0)
    {
        error2.innerHTML='enter password'
        error2.style.margin='0px'
        result=false
    }
    else{
        error2.innerHTML=''
        error2.style.margin='5px'
    }
    if(inputObj[3].value.length==0)
    {
        error3.innerHTML='enter name'
        error3.style.margin='0px'
        result=false
    }
    else{
        error3.innerHTML=''
        error3.style.margin='5px'
    }

    return result
}