(function () {
    const levels = [
        {
            level: 1,
            name: "Niveau 1 : 4 chiffres",
            time: 30,
            bonusMode: false, // Progressif
            totalPoints: 2,
            passwords: [
                { password: "1950", hint: "Son année de naissance" },
                { password: "1975", hint: "Année de naissance de Nathalie" },
                { password: "0350", hint: "Mois + deux derniers chiffres de l'année" },
                { password: "2004", hint: "Jour et mois de naissance de Nathalie" },
            ]
        },
        {
            level: 2,
            name: "Niveau 2 : 4 lettres + 2 chiffres",
            time: 40,
            bonusMode: false, // Progressif
            totalPoints: 2,
            passwords: [
                { password: "bleu03", hint: "Sa couleur préférée + jour de naissance" },
                { password: "lidl01", hint: "Lieu de travail + jour de naissance" },
                { password: "mich50", hint: "Son prénom + deux chiffres de naissance" },
                { password: "pyth03", hint: "Son animal préféré + mois de naissance" },
            ]
        },
        {
            level: 3,
            name: "Niveau 3 : 6 caractères (lettres + chiffres)",
            time: 45,
            bonusMode: true, // Tout ou rien
            totalPoints: 1,
            passwords: [
                { password: "cobra3", hint: "Son animal + nombre qu'elle possède" },
                { password: "foot57", hint: "Son sport préféré + département" },
                { password: "57lidl", hint: "Son métier d'avant + année" },
                { password: "guill9", hint: "Nom de son fils + année" },
            ]
        },
        {
            level: 4,
            name: "Niveau 4 : 6 caractères + symboles",
            time: 50,
            bonusMode: true, // Tout ou rien
            totalPoints: 1,
            passwords: [
                { password: "gym@75", hint: "Sport de Nathalie + @ + année de naissance" },
                { password: "art79!", hint: "Passion de Guillaume + année + !" },
                { password: "lid@50", hint: "Travail + symbole + année" },
                { password: "py@03!", hint: "Animal + @ + mois + !" },
            ]
        },
        {
            level: 5,
            name: "Niveau 5 : 8 caractères",
            time: 60,
            bonusMode: true, // Tout ou rien
            totalPoints: 1,
            passwords: [
                { password: "ch@te@u1", hint: "Lieu d'héritage avec des @ et chiffres" },
                { passwordSZ: "lidl7579", hint: "Travail + années de naissance des enfants" },
                { password: "pyth@1950", hint: "Animal + symbole + année" },
                { password: "neuilly92", hint: "Ville + code département" },
            ]
        }
    ];

    let remaining = [], totalScore = 0, hintsUsed = 0, elapsedTime = 0, timerInterval = null;
    let showHintFlag = false, skippedPasswords = [], levelProgress = {};

    const $ = id => document.getElementById(id);

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
                // Tout ou rien
                if (found === total) {
                    score += l.totalPoints;
                }
            } else {
                // Progressif
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

        // Chronomètre
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

        // Afficher le mode de points
        const levelConfig = levels.find(l => l.level === target.level);
        const modeText = levelConfig.bonusMode ? " 🎁 BONUS (tout ou rien)" : " 📊 Progressif";
        $("password-number").textContent = `Mot de passe (${levelProgress[target.level].found}/${levelProgress[target.level].total}) ${modeText}`;

        passwordInput.value = "";
        hintEl.classList.add("hidden"); hintEl.textContent = "";
        showHintFlag = false; hintBtn.disabled = false;
        feedbackEl.classList.add("hidden"); feedbackEl.textContent = "";
        updateProgress();
    }

    function checkPassword() {
        const input = passwordInput.value.trim(); if (!input) return;
        const idx = remaining.findIndex(r => r.password === input);
        if (idx === -1) { showFeedback("Mot de passe incorrect, réessayez !", false); return; }

        const found = remaining[idx];
        levelProgress[found.level].found++;

        totalScore = calculateScore();
        scoreEl.textContent = totalScore.toFixed(2);

        showFeedback(`Correct ! Score recalculé.`, true);
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
        showFeedback("Niveau sauté.", false);
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

        totalScore = calculateScore(); // Recalcul final
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

        maxScoreText.textContent = `points sur 7 possibles`;
        percentageEl.textContent = Math.round((totalScore / 7) * 100) + "%";
        hintsUsedEl.textContent = hintsUsed > 0 ? `💡 Indices utilisés : ${hintsUsed}` : "";

        if (enableTimerCheckbox.checked) {
            const timeDiv = document.createElement("p");
            timeDiv.textContent = `⏱️ Temps écoulé : ${formatTime(elapsedTime)}`;
            timeDiv.style.marginTop = "10px";
            timeDiv.style.color = "#6b7280";
            endScreen.insertBefore(timeDiv, replayBtn.parentElement);
        }

        // Détail des scores par niveau
        const detailDiv = document.createElement("div");
        detailDiv.style.marginTop = "15px";
        detailDiv.style.textAlign = "left";
        detailDiv.style.background = "#f3f4f6";
        detailDiv.style.padding = "15px";
        detailDiv.style.borderRadius = "8px";
        let detailText = "📊 Détail par niveau :\n\n";
        levels.forEach(l => {
            const found = levelProgress[l.level].found;
            const total = levelProgress[l.level].total;
            let earnedPoints = 0;
            if (l.bonusMode) {
                earnedPoints = found === total ? l.totalPoints : 0;
                detailText += `${l.name} : ${found}/${total} mots → ${earnedPoints}/${l.totalPoints} pts ${found === total ? '🎁' : '❌'}\n`;
            } else {
                earnedPoints = (found / total) * l.totalPoints;
                detailText += `${l.name} : ${found}/${total} mots → ${earnedPoints.toFixed(2)}/${l.totalPoints} pts 📊\n`;
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
            let text = "Mots de passe manqués :\n";
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