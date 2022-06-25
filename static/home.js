let a=1
let b1=document.querySelector('#previousbutton')
let b2=document.querySelector('#nextbutton')
let img1=document.querySelector('#img1')
let img2=document.querySelector('#img2')
let img3=document.querySelector('#img3')
b1.addEventListener('click', function(){
    if(a>1){
        if(a===2){
            img1.style.display='block'
            img2.style.display='none'
            img3.style.display='none'

        }
        if(a===3){
            img1.style.display='none'
            img2.style.display='block'
            img3.style.display='none'
        }
        a=a-1
    }
})
b2.addEventListener('click', function(){
    if(a<3){
        if(a===1){
            img1.style.display='none'
            img2.style.display='block'
            img3.style.display='none'

        }
        if(a===2){
            img1.style.display='none'
            img2.style.display='none'
            img3.style.display='block'
        }
        a=a+1
    }
})
