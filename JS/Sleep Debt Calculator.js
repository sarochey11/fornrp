const getSleepHours = (day) => {
    switch (day) {
        case 'Monday':
            return 8;
        case 'Tuesday':
            return 7;
        case 'Wednesday':
            return 8;
        case 'Thursday':
            return 8;
        case 'Friday':
            return 8;
        case 'Saturday':
            return 8;
        case 'Sunday':
            return 8;
        default:
            return 'Invalid day';
    }
}

const getActualSleepHours = () => {
    return getSleepHours('Monday') + getSleepHours('Tuesday') + getSleepHours('Wednesday') + getSleepHours('Thursday') + getSleepHours('Friday') + getSleepHours('Saturday') + getSleepHours('Sunday');
}

const getIdealSleepHours = () => {
    const idealHours = 8;
    return idealHours * 7;
}

const calculateSleepDebt = () => {
    const getActualSleepHours = getActualSleepHours();
    const getIdealSleepHours = getIdealSleepHours();
    if (getActualSleepHours() === getIdealSleepHours()) {
        console.log('You got the perfect amount of sleep!');
    } else if (getActualSleepHours() > getIdealSleepHours()) {
        console.log('You got more sleep than needed');
    } else {
        console.log('You got less sleep than needed');
    }
};

if (actualSleepHours < idealSleepHours) {
    console.log('You got ' + (idealSleepHours - actualSleepHours) + ' hour(s) less sleep than needed this week. Get some rest.');
}

calculateSleepDebt();