(function () {
    const levels = [
        {
            level: 1,
            // Translation: Level 1: 4 digits
            name: "Level 1: 4 digits",
            time: 30,
            // Translation: Progressive
            bonusMode: false, // Progressive
            totalPoints: 2,
            passwords: [
                // Translation: His birth year
                { password: "1950", hint: "His birth year" },
                // Translation: Nathalie's birth year
                { password: "1975", hint: "Nathalie's birth year" },
                // Translation: Month + last two digits of the year
                { password: "0319", hint: "Month + last two digits of the year" },
                // Translation: Nathalie's birth day and month
                { password: "2004", hint: "Nathalie's birth day and month" },
            ]
        },
        {
            level: 2,
            // Translation: Level 2: 4 letters + 2 digits
            name: "Level 2: 4 letters + 2 digits",
            time: 40,
            // Translation: Progressive
            bonusMode: false, // Progressive
            totalPoints: 2,
            passwords: [
                // Translation: Her favorite color + birth day
                { password: "bleu03", hint: "Her favorite color + birth day" },
                // Translation: Workplace + birth day
                { password: "lidl01", hint: "Workplace + birth day" },
                // Translation: Her first name + last two birth digits
                { password: "mich50", hint: "Her first name + last two birth digits" },
                // Translation: Her favorite animal + birth month
                { password: "pyth03", hint: "Her favorite animal + birth month" },
            ]
        },
        {
            level: 3,
            // Translation: Level 3: 6 characters (letters + digits)
            name: "Level 3: 6 characters (letters + digits)",
            time: 45,
            // Translation: All or nothing
            bonusMode: true, // All or nothing
            totalPoints: 1,
            passwords: [
                // Translation: Her animal + number she possesses
                { password: "cobra3", hint: "Her animal + number she owns" },
                // Translation: Her favorite sport + department
                { password: "foot57", hint: "Her favorite sport + department" },
                // Translation: Her previous job + year
                { password: "vente50", hint: "Her previous job + year" },
                // Translation: Guillaume's hobby + year
                { password: "retro79", hint: "Guillaume's hobby + year" },
            ]
        },
        {
            level: 4,
            // Translation: Level 4: 6 characters + symbols
            name: "Level 4: 6 characters + symbols",
            time: 50,
            // Translation: All or nothing
            bonusMode: true, // All or nothing
            totalPoints: 1,
            passwords: [
                // Translation: Nathalie's sport + @ + birth year
                { password: "gym@75", hint: "Nathalie's sport + @ + birth year" },
                // Translation: Guillaume's hobby + year + !
                { password: "art79!", hint: "Guillaume's hobby + year + !" },
                // Translation: Work + symbol + year
                { password: "lid@50", hint: "Work + symbol + year" },
                // Translation: Animal + @ + month + !
                { password: "py@03!", hint: "Animal + @ + month + !" },
            ]
        },
        {
            level: 5,
            // Translation: Level 5: 8 characters
            name: "Level 5: 8 characters",
            time: 60,
            // Translation: All or nothing
            bonusMode: true, // All or nothing
            totalPoints: 1,
            passwords: [
                // Translation: Inheritance location with @ and digits
                { password: "ch@te@u1", hint: "Inheritance location with @ and digits" },
                // Translation: Work + children's birth years
                { password: "lidl7579", hint: "Work + children's birth years" },
                // Translation: Animal + symbol + year
                { password: "pyth@1950", hint: "Animal + symbol + year" },
                // Translation: City + department code
                { password: "neuilly92", hint: "City + department code" },
            ]
        }
    ];

    let remaining = [], totalScore = 0, hintsUsed = 0, elapsedTime = 0, timerInterval = null;
    let showHintFlag = false, skippedPasswords = [], levelProgress = {};

    const $ = id => document.getElementById(id);

    // Variable naming reflects the French HTML IDs, which is standard practice when
    // translating code based on existing structure.
    const startScreen = $("start-screen"),
        gameScreen = $("game-screen"),
        endScreen = $("end-screen"),
        startBtn = $("start-button"),
        validateBtn = $("validate-btn"),
        hintBtn = $("hint-btn"),
        skipBtn = $("skip-btn"),
        togglePwdBtn = $("toggle-password-btn"),
        passwordInput = $("password-input"),
        timerSpan = $("timer"),
        timerDisplay = $("timer-display"),
        scoreEl = $("score"),
        feedbackEl = $("feedback"),
        hintEl = $("hint"),
        progressText = $("progress-text"),
        progressBar = $("progress-bar"),
        foundList = $("found-passwords-list"),
        levelTitle = $("level-title"),
        finalScoreEl = $("final-score"),
        maxScoreText = $("max-score-text"),
        percentageEl = $("percentage"),
        hintsUsedEl = $("hints-used"),
        replayBtn = $("replay-btn"),
        enableTimerCheckbox = $("disable-timer"),
        skippedDiv = $("skipped-passwords"),
        skippedList = $("skipped-list");

    function buildRemaining() {
        remaining = [];
        levelProgress = {};
        levels.forEach(l => {
            levelProgress[l.level] = { found: 0, total: l.passwords.length };
            l.passwords.forEach(p => remaining.push({
                level: l.level,
                name: l.name,
                password: p.password,
                hint: p.hint,
                bonusMode: l.bonusMode,
                totalPoints: l.totalPoints,
                passwordCount: l.passwords.length
            }));
        });
    }

    function formatTime(seconds) {
        const mins = Math.floor(seconds / 60);
        const secs = seconds % 60;
        return `${mins}:${secs.toString().padStart(2, '0')}`;
    }

    function calculateScore() {
        let score = 0;
        levels.forEach(l => {
            const found = levelProgress[l.level].found;
            const total = levelProgress[l.level].total;

            if (l.bonusMode) {
                // All or nothing
                if (found === total) {
                    score += l.totalPoints;
                }
            } else {
                // Progressive
                score += (found / total) * l.totalPoints;
            }
        });
        return score;
    }

    function startGame() {
        buildRemaining();
        totalScore = 0; hintsUsed = 0; showHintFlag = false; skippedPasswords = []; elapsedTime = 0;
        startScreen.classList.add("hidden");
        endScreen.classList.add("hidden");
        gameScreen.classList.remove("hidden");
        foundList.innerHTML = "";
        skippedList.innerHTML = "";
        skippedDiv.classList.add("hidden");

        // Chronometer (Timer)
        clearInterval(timerInterval); timerInterval = null;
        if (enableTimerCheckbox.checked) {
            timerSpan.textContent = formatTime(0);
            timerDisplay.classList.remove("warning", "danger");
            timerInterval = setInterval(() => {
                elapsedTime++;
                timerSpan.textContent = formatTime(elapsedTime);
            }, 1000);
        } else {
            timerSpan.textContent = "—";
            timerDisplay.classList.remove("warning", "danger");
        }

        loadNextTarget();
    }

    function loadNextTarget() {
        if (remaining.length === 0) return endGame();
        const target = remaining[0];
        levelTitle.textContent = target.name;

        // Display points mode
        const levelConfig = levels.find(l => l.level === target.level);
        // Translation: BONUS (all or nothing) / Progressive
        const modeText = levelConfig.bonusMode ? " 🎁 BONUS (all or nothing)" : " 📊 Progressive";
        // Translation: Password
        $("password-number").textContent = `Password (${levelProgress[target.level].found}/${levelProgress[target.level].total}) ${modeText}`;

        passwordInput.value = "";
        hintEl.classList.add("hidden"); hintEl.textContent = "";
        showHintFlag = false; hintBtn.disabled = false;
        feedbackEl.classList.add("hidden"); feedbackEl.textContent = "";
        updateProgress();
    }

    function checkPassword() {
        // Translation: Incorrect password, try again!
        const input = passwordInput.value.trim(); if (!input) return;
        const idx = remaining.findIndex(r => r.password === input);
        if (idx === -1) { showFeedback("Incorrect password, try again!", false); return; }

        const found = remaining[idx];
        levelProgress[found.level].found++;

        totalScore = calculateScore();
        scoreEl.textContent = totalScore.toFixed(2);

        // Translation: Correct! Score recalculated.
        showFeedback(`Correct! Score recalculated.`, true);
        const li = document.createElement("li");
        li.textContent = `${found.name} — ${found.password}`;
        foundList.appendChild(li);

        remaining.splice(idx, 1);
        setTimeout(loadNextTarget, 600);
    }

    function showFeedback(msg, ok) {
        feedbackEl.textContent = (ok ? "✓ " : "✗ ") + msg;
        feedbackEl.className = "feedback " + (ok ? "success" : "error");
        feedbackEl.classList.remove("hidden");
    }

    function useHint() {
        if (showHintFlag || remaining.length === 0) return;
        showHintFlag = true;
        const target = remaining[0];
        hintEl.textContent = "💡 " + target.hint;
        hintEl.classList.remove("hidden");
        totalScore = Math.max(0, +(totalScore - 0.05).toFixed(2));
        scoreEl.textContent = totalScore.toFixed(2);
        hintsUsed++;
        hintBtn.disabled = true;
    }

    function skipTarget() {
        if (remaining.length === 0) return;
        const currentLevel = remaining[0].level;
        const toSkip = remaining.filter(r => r.level === currentLevel);
        skippedPasswords.push(...toSkip);
        remaining = remaining.filter(r => r.level !== currentLevel);
        // Translation: Level skipped.
        showFeedback("Level skipped.", false);
        updateSkippedDisplay();
        setTimeout(loadNextTarget, 400);
    }

    function updateSkippedDisplay() {
        if (skippedPasswords.length === 0) {
            skippedDiv.classList.add("hidden");
            skippedList.innerHTML = "";
            return;
        }
        skippedDiv.classList.remove("hidden");
        skippedList.innerHTML = "";
        skippedPasswords.forEach(p => {
            const li = document.createElement("li");
            li.textContent = `${p.name} — ${p.password}`;
            skippedList.appendChild(li);
        });
    }

    function updateProgress() {
        const total = levels.reduce((s, l) => s + l.passwords.length, 0);
        const done = total - remaining.length;
        progressText.textContent = `${done} / ${total}`;
        progressBar.style.width = (done / total) * 100 + "%";
    }

    function endGame() {
        clearInterval(timerInterval); timerInterval = null;
        gameScreen.classList.add("hidden");
        endScreen.classList.remove("hidden");

        totalScore = calculateScore(); // Final recalculation
        finalScoreEl.textContent = totalScore.toFixed(2);

        const results = {
            score: totalScore,
            skipped: skippedPasswords,
            hintsUsed: hintsUsed,
            time: elapsedTime,
            date: new Date().toISOString()
        };
        localStorage.setItem("gameResults", JSON.stringify(results));
        launchConfetti();

        // Translation: points out of 7 possible
        maxScoreText.textContent = `points out of 7 possible`;
        percentageEl.textContent = Math.round((totalScore / 7) * 100) + "%";
        // Translation: Hints used
        hintsUsedEl.textContent = hintsUsed > 0 ? `💡 Hints used: ${hintsUsed}` : "";

        if (enableTimerCheckbox.checked) {
            const timeDiv = document.createElement("p");
            // Translation: Elapsed Time
            timeDiv.textContent = `⏱️ Elapsed Time: ${formatTime(elapsedTime)}`;
            timeDiv.style.marginTop = "10px";
            timeDiv.style.color = "#6b7280";
            endScreen.insertBefore(timeDiv, replayBtn.parentElement);
        }

        // Translation: Score details by level
        const detailDiv = document.createElement("div");
        detailDiv.style.marginTop = "15px";
        detailDiv.style.textAlign = "left";
        detailDiv.style.background = "#f3f4f6";
        detailDiv.style.padding = "15px";
        detailDiv.style.borderRadius = "8px";
        // Translation: Score details by level:
        let detailText = "📊 Score details by level:\n\n";
        levels.forEach(l => {
            const found = levelProgress[l.level].found;
            const total = levelProgress[l.level].total;
            let earnedPoints = 0;
            if (l.bonusMode) {
                earnedPoints = found === total ? l.totalPoints : 0;
                // Translation: passwords -> pts
                detailText += `${l.name} : ${found}/${total} passwords → ${earnedPoints}/${l.totalPoints} pts ${found === total ? '🎁' : '❌'}\n`;
            } else {
                earnedPoints = (found / total) * l.totalPoints;
                // Translation: passwords → pts
                detailText += `${l.name} : ${found}/${total} passwords → ${earnedPoints.toFixed(2)}/${l.totalPoints} pts 📊\n`;
            }
        });
        detailDiv.style.whiteSpace = "pre-line";
        detailDiv.textContent = detailText;
        endScreen.insertBefore(detailDiv, replayBtn.parentElement);

        if (skippedPasswords.length > 0) {
            const div = document.createElement("div");
            div.style.whiteSpace = "pre-line";
            div.style.marginTop = "15px";
            div.style.textAlign = "left";
            div.style.background = "#fff7ed";
            div.style.padding = "15px";
            div.style.borderRadius = "8px";
            div.style.borderLeft = "4px solid #f59e0b";
            // Translation: Skipped passwords:
            let text = "Skipped passwords:\n";
            skippedPasswords.forEach(p => { text += `- ${p.name} : ${p.password}\n`; });
            div.textContent = text;
            endScreen.insertBefore(div, replayBtn.parentElement);
        }
    }

    function launchConfetti() {
        const duration = 3000, end = Date.now() + duration;
        (function frame() {
            confetti({ particleCount: 4, spread: 60 });
            if (Date.now() < end) requestAnimationFrame(frame);
        })();
    }

    function togglePasswordVisibility() {
        passwordInput.type = passwordInput.type === "password" ? "text" : "password";
    }

    function replay() {
        const extras = endScreen.querySelectorAll("div[style], p[style]");
        extras.forEach(el => el.remove());
        endScreen.classList.add("hidden");
        startScreen.classList.remove("hidden");
    }

    startBtn.addEventListener("click", startGame);
    validateBtn.addEventListener("click", checkPassword);
    hintBtn.addEventListener("click", useHint);
    skipBtn.addEventListener("click", skipTarget);
    togglePwdBtn.addEventListener("click", togglePasswordVisibility);
    replayBtn.addEventListener("click", replay);
    passwordInput.addEventListener("keydown", e => { if (e.key === "Enter") checkPassword(); });
})();