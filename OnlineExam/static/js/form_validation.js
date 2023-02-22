function validation(){
    result=true
    queObj=document.getElementsByTagName('textarea')
    
    selectObj=document.getElementById('select')
    if(queObj[0].value.length==0)
    {
        errorObj=document.getElementById('question')
        errorObj.innerHTML="This field can't be empty";
        errorObj.style.margin='0px';
        result=false
    }
    else{
        errorObj=document.getElementById('question')
        errorObj.style.margin='15px';
        errorObj.innerHTML="";
    }
    optiona=document.getElementById('optiona')
    if(document.getElementById('a').value.length==0)
    {
        optiona.innerHTML='Enter optiona'
        optiona.style.margin='0px'
        result=false
    }
    else{
        optiona.innerHTML=''
        optiona.style.margin='15px'
    }
    optionb=document.getElementById('optionb')
    if(document.getElementById('b').value.length==0)
    { 
       optionb.innerHTML='enter optionb'
       optionb.style.margin='0px'
       result=false
    }
    else{
       optionb.innerHTML=''
       optionb.style.margin='15px'
    }
    optionc=document.getElementById('optionc')
    if(document.getElementById('c').value.length==0)
    {
        optionc.innerHTML='enter optionc'
        optionc.style.margin='0px'
        result=false
    }
    else{
       optionc.innerHTML=''
       optionc.style.margin='15px'
    }
    optiond=document.getElementById('optiond')
    if(document.getElementById('d').value.length==0)
    {
        optiond.innerHTML='enter optiond'
        optiond.style.margin='0px'
        result=false
    }
    else{
        optiond.innerHTML=''
        optiond.style.margin='15px'
    }
    select=document.getElementById('answer')
    if(document.getElementById('select').value=='e')
    {
        select.innerHTML='select answer'
        select.style.margin='0px'
        result=false
    }
    else{
       select.innerHTML=''
       select.style.margin='15px'
    }
     if(result)
     {
        $('#questionForm').submit(serverRequest)
        
     }
     else{
       return false;
     }
     return false
    // return result
   
}

function serverRequest(event)
{
    obj={}
    // event.preventDefautl
    console.log($(this).serializeArray())
    let data=$(this).serializeArray()
    data.reduce((obj,e)=>{
        obj[e.name]=e.value
        return obj
    },obj)
    console.log(obj)
    $.ajax({
        mathod:"POST",
        url:"{% url 'Newquestion' }",
        data:obj,
        success:function(response){
           alert("am"); 
        }
    })
    .done(function(response){
       console.log(response)    
    })
    .fail(function(response){
        console.log(response)  
    })
}



