document.addEventListener("DOMContentLoaded", function() {

// GRAB META TAG WHOSE NAME IS CSRF-TOKEN
const csrfToken = document.querySelector('meta[name="csrf-token"]').content;

async function handle_comment_likes(commentid) {
    
    const response = await fetch(`/blog/details/${commentid}/comment/like/`,{
        method: "POST",
        headers: {
            "X-CSRFToken": csrfToken
        }

    });

    if(!response.ok){
      console.log("Request Failed", response.status);
      return;  
    }

    const data = await response.json();
    return data
}

async function handle_post_likes(postid) {
        // FETCH LIKES DATA
        const response = await fetch(`/blog/details/${postid}/like/`,{
            method:"POST",
            headers:{
                "X-CSRFToken": csrfToken
            }
        })
        // HANDLE ERROR
        if(!response.ok){
            console.log("Request Failed", response.status);
            return;
        }

        const data = await response.json();
        return data;
    }

async function handle_registration() {

    const response = await fetch("",{

    })

    const data = await response.status()
    
    return data
}   

const btn = document.querySelector(".btn");

btn.addEventListener("click", async function() {
    // console.log("yooo")
    const postid = this.dataset.postId;
 
    data = await handle_post_likes(postid);
 
    const likeCount = document.querySelector("#like-count");
    // let count = Number(likeCount.textContent);

    if (data.liked) {
        this.innerHTML = "&#9829;"
    }else {
        this.innerHTML = "&#9825;"
    }
    likeCount.textContent = data.count;
 
})

const comment_btn = document.querySelectorAll(".comment-like-btn");

comment_btn.forEach(function(c_btc) {
    c_btc.addEventListener("click", async function() {

    const commentid = this.dataset.commentId;

    console.log("Button clicked", commentid);

    const data = await handle_comment_likes(commentid);

    console.log("Fetch completed");
    console.log("worked")
    console.log("Request data =", data);

    let likeCount = this.nextElementSibling.querySelector(".c-like-count");


    if(data.liked) {
       this.innerHTML = "&#9829;" 
    }else {
        this.innerHTML = "&#9825;"
    }
    
    likeCount.textContent = data.count;
    
    
})

})





})