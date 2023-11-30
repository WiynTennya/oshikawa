const maincontainer = document.querySelector(".main-container"),
    imagePreview = maincontainer.querySelectorAll(".image-preview"),
    images = maincontainer.querySelectorAll(".image-preview img")
    video = maincontainer.querySelectorAll("video")

window.onload = () => {
    maincontainer.onmouseenter = () => {
        images.forEach((image) => {
            image.style.opacity = 0.5;
        })
    }
    maincontainer.onmouseleave = () => {
        images.forEach((image) => {
            image.style.opacity = 1;
        })
    }

    let tl = gsap.timeline();

    tl.to(imagePreview, {
        duration: 1,
        clipPath: "polygon(0 0, 100% 0%, 100% 100%, 0% 100%)",
        stagger: 0.1
    })
    
}