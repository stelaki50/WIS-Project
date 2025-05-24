<!--SERVICES PAGE-->

<script>


</script>

<style>

:root
{
    --bg-color: #8FD6E3;
    --typewriterSpeed: 6s;
    --typewriterCharacters: 23;
}

main{
	background-color: #8FD6E3;
	height: 100%;
    font-family: 'Ubuntu';
    margin: 0;
    min-height: 40vh;
    display: grid;
    place-content: center;
    text-align: center;
    background: var(--bg-color);
}

h1
{
    font-size: clamp(1rem, 2vw + 1rem, 4rem);
    position: relative;
    margin: 0 auto;
    margin-top: 3%;
    font-family: "Ubuntu", monospace;
    width: max-content;
}

h1::before, h1::after
{
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
}

h1::before
{
    background: var(--bg-color);
    animation: typewriter var(--typewriterSpeed) steps(var(--typewriterCharacters)) 3s forwards;
}

h1::after
{
    width: 0.125em;
    background: black;
    animation: typewriter var(--typewriterSpeed) steps(var(--typewriterCharacters)) 3s forwards,  
    blink 600ms steps(23) infinite;
}

.subtitle
{
    color: hsl(0 0% 0% / 0.7);
    font-size: 2rem;
    font-weight: 400;
    opacity: 0;
    transform: translateY(3rem);
    animation: fadeInUp 2s ease calc(var(--typewriterSpeed) + 2s) forwards;
}

@keyframes typewriter
{
    to 
    {
        left: 100%;
    }
}

@keyframes blink
{
    to
    {
        background: transparent;
    }
}

@keyframes fadeInUp
{
    to
    {
        opacity: 1;
        transform: translateY(0);
    }
}

/*content*/
.content
{
    margin-top: 5%;
    display: grid;
    grid-template-rows: repeat(4, 1fr);
    grid-gap: 10px;
}

img
{
    border-radius: 10px;
}

.first_img, .third_img, .fifth_img
{
    float: left;
}

.second_img, .fourth_img
{
    float: right;
}

.section1
{
    border-radius: 10px;
    box-shadow: 5px 5px 5px 5px rgba(0, 0, 0, 0.7);
}

.section2
{
    border-radius: 10px;   
}

.section3
{
    border-radius: 10px;
    box-shadow: 5px 5px 5px 5px rgba(0, 0, 0, 0.7);
}

.section4
{
    border-radius: 10px;
}

.section5
{
    border-radius: 10px;
    box-shadow: 5px 5px 5px 5px rgba(0, 0, 0, 0.7);
}

.section1-p, .section2-p, .section3-p, .section4-p, .section5-p
{
    font-family: 'Ubuntu', cursive;
    font-size: 2em;
    text-align: center;
    align-items: center;
    justify-content: center;
    align-content: center;    
}


</style>

<main>
    
    <h1>What you dream, we can make it real for you.</h1>
    <p class="subtitle"><b>Discover the potential of our glorious team!</b></p>

    <div class="content">

        <div class="section1">

            <img src="/images/services_photos/pc_build_hands.jpg" alt="pc_building_hands" width="400" height="300" class="first_img">
            <p class="section1-p">Behind every powerful PC we build is a pair of skilled hands and a 
                passion for technology. We don’t just assemble parts; we craft the heartbeat of your digital world.
                Precision meets passion—our experts meticulously assemble every PC with care and expertise. 
                Whether it's for gaming, creative work, or high-performance tasks, we build machines that are not just powerful, but personal.</p>


        </div>

        <div class="section2">

            <img src="/images/services_photos/pc_repair.jpg" alt="pc_repair" width="400" height="300" class="second_img">
            <p class="section2-p">Our dedicated repair team brings years of hands-on experience to every 
                hardware challenge. From diagnosing faulty components to restoring full system functionality, 
                we treat every device with the care and precision it deserves. Whether it’s a damaged motherboard, 
                overheating issue, or faulty RAM, our hardware technicians are equipped with the tools and 
                knowledge to restore your system efficiently and reliably.</p>

        </div>

        <div class="section3">

            <img src="/images/services_photos/pc_software.jpg" alt="pc_software" width="400" height="300" class="third_img">
            <p class="section3-p">From removing stubborn viruses to installing the latest software suites, our team handles it 
                all with precision. Whether it's a performance tune-up or a full system setup, we ensure your software runs 
                smoothly and securely. We specialize in operating system reinstalls, driver updates, and application 
                troubleshooting. No crashes, no conflicts—just clean, efficient software tailored to your system's needs.</p>

        </div> 

        <div class="section4">

            <img src="/images/services_photos/pc_troubleshoot.jpg" alt="pc_troubleshoot" width="400" height="300" class="fourth_img">
            <p class="section4-p">Not sure what’s wrong with your device? Our diagnostics team dives deep to pinpoint the issue
                fast—no guesswork, just accurate analysis and clear solutions you can trust. </p>
        </div>

        <h2 style="font-family: 'Ubuntu';">Click <a href="/about">here</a> if you want any of the above services and our team will respond less than 12 hours!</h2>
</main>
