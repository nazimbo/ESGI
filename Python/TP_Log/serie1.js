Highcharts.chart('serie1',
{
        chart: {
            type: 'pie'
        },
		title: {
			text: 'Part de marché des navigateurs'
		},
		subtitle: {
			text: '... dans un monde idéal'
		},
        series: [{
            data: [
					['Firefox', 54],
					['Chrome', 17],
					['Edge', 16],
					['Opera', 4],
					['Safari', 3],
					['Autres', 6],
        ]
        }]
    });
