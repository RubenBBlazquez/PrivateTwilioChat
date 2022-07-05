/**
 *
 */

document.getElementById('menu_icon').addEventListener('click',() => openMenu())

const openMenu  = () =>{

    console.log("benas tardes")

    const menu = document.getElementById('sidebarMenu')
    menu.setAttribute('class','openModal')

    console.log(menu)
}