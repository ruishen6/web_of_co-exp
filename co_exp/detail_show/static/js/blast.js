$(document).ready(function() {
	$("#selectBlastFile").click(function() {
		if(document.all) {
			document.getElementById("blastFile").click();
		}
		else {
			var bt=document.getElementById("blastFile");
			bt.click();  
		}
    });
    // $('#selectBlastFile').click(function(){
    //     if (window.File && window.FileReader && window.FileList && window.Blob) {
    //         console.log( 'browser ok' )
    //         $('#blastFile').click();
    //     } else {
    //         showOverlay("Your current browser does not support file uploads\n\rPlease update or change a browser\n\rIt is recommended to use Google/firefox");
    //         return;
    //     }
    // });
	$("#blastFile").change(function() {
		$("#blastFileCopy").val($("#blastFile").val());
    });
    
    // example sequences for testing
    var ex_nucleotide = ">CLEC010822-RA:cDNA , Heat shock protein 70-2\n" +
        "TGGAAATTTAAATATTTTCGATTTGGCGCGCCTTTAAGCCGGCGCCC" +
        "AATCGCGTTTCGGAACGTATTGTCAGTCAGCCGGACCAATCAACGCC" +
        "GTCCACGATTCCCGACTTCTCCCCGTCACCCAACCCCATTCTTATTC" +
        "CACAGCCGCGGCCGTTCGTCCGTTCAGTCGAACCTAGGACTTGATTC" +
        "GAGTACAAAGCGGACGAAAAAACGCGAATTAAACATAGTGTCTTATT" +
        "CTTAATTTTGATCTAGTTGAAAACAAAAAAAGAGAGAAGGGTATATT" +
        "TTTTTATATTTTCGAGTCAGTTGTATCAAAAATCAAACCGGAATAAT" +
        "TCAGAGATTTTCACAATAATGATTTTACATTTTCTCGTTTTGCTTTT" +
        "CGCTTCGGCCTTAGCAGCCGACGAGAAGAATAAGGACGTCGGAACCG" +
        "TCGTGGGCATTGACCTCGGCACGACTTACTCTTGTGTGGGAGTGTAC" +
        "AAGAATGGAAGAGTTGAAATCATCGCCAACGATCAAGGAAACAGGAT" +
        "TACACCTTCATACGTCGCTTTCACCAGTGAAGGCGAGCGTCTTATCG" +
        "GAGATGCCGCCAAGAATCAGTTGACGACCAACCCTGAAAACACCGTC" +
        "TTCGACGCTAAGCGTCTTATCGGACGAGAATGGACGGACAGCACTGT" +
        "TCAAGACGATATCAAGTTCTTCCCATTCAAAGTCTTGGAGAAAAATA" +
        "GCAAGCCTCACATTCAAGTCTCCACGTCCCAGGGCAACAAAATGTTC" +
        "GCACCCGAAGAAATCTCCGCTATGGTATTGGGTAAAATGAAAGAGAC" +
        "GGCAGAGGCATATTTGGGAAAGAAGGTCACCCACGCCGTAGTCACAG" +
        "TACCCGCATACTTCAACGATGCCCAGAGGCAGGCAACAAAAGATGCT" +
        "GGAACGATTTCAGGACTCAACGTCATGAGGATCATCAACGAACCGAC" +
        "CGCAGCAGCTATTGCTTACGGACTGGACAAGAAAGAAGGAGAAAAGA" +
        "ACGTACTCGTTTTTGATCTCGGCGGTGGTACTTTTGATGTATCTCTT" +
        "CTCACCATCGACAACGGAGTTTTCGAAGTCGTTTCTACAAACGGTGA" +
        "TACTCACTTAGGAGGAGAGGACTTTGATCAAAGGGTTATGGACCACT" +
        "TTATTAAACTGTACAAGAAGAAGAAGGGCAAGGATATCAGGAAAGAC" +
        "AACAGGGCTGTTCAGAAACTCAGGAGGGAAGTCGAAAAAGCAAAGAG" +
        "GGCTCTGTCTTCTAGCCACCAGGTCAGGATAGAAATTGAAAGCTTCT" +
        "ATGACGGTGAAGACTTCTCTGAGACTCTCACTAGGGCAAAATTCGAA" +
        "GAGCTCAACATGGACCTCTTCCGTTCCACCATGAAACCCGTTCAGAA" +
        "GGTCCTCGAAGATGCTGACATGAACAAGAAAGACGTCGATGAAATTG" +
        "TTTTAGTAGGAGGCAGCACCAGGATTCCAAAAGTTCAGGCCCTCGTC" +
        "AAAGAGTTTTTCAACGGAAAAGAACCATCCCGAGGTATCAACCCCGA" +
        "TGAAGCTGTCGCTTATGGAGCAGCAGTTCAAGCTGGAGTTTTATCTG" +
        "GTGAACAAGACACCGATTCAATCGTCCTCCTTGATGTCAACCCTCTG" +
        "ACCCTCGGAATCGAAACAGTCGGTGGTGTCATGACCAAACTCATCCC" +
        "AAGGAACACAGTCATCCCGACGAAAAAATCTCAGATCTTCTCGACAG" +
        "CTTCAGACAACCAACACACTGTCACCATTCAGGTTTATGAGGGAGAA" +
        "AGGCCAATGACCAAAGATAATCATTTGCTCGGAAAATTCGATTTGAC" +
        "AGGAATACCGCCTGCACCAAGGGGAGTGCCACAGATTGAAGTCACTT" +
        "TTGAGATCGATGCCAACGGTATCCTTCAGGTGTCCGCCGAGGACAAG" +
        "GGAACGGGCAACAGAGAGAAAATAGTCATCACAAACGACCAGAACAG" +
        "GTTGACTCCAGACGACATCGATAGGATGATCAAGGACGCCGAGAAGT" +
        "TCGCTGATGACGACAAGAAGCTCAAGGAGCGCGTCGAGGCCAGGAAC" +
        "GAACTGGAGTCGTACGCCTATTCTCTCAAGAACCAGCTCGCCGACAA" +
        "GGACAAGTTCGGATCGAAGGTGACGGATTCTGACAAGGCCAAGATGG" +
        "AAAAAGCCATCGAAGAGAAAATCAAGTGGCTTGACGAGAACCAAGAC" +
        "GCCGACAGTGAAGCCTTCAAGAAGCAAAAGAAAGAACTCGAAGATGT" +
        "CGTACAGCCCATCATCTCAAAATTATACCAAGGAGGTGCTCCGCCGC" +
        "CACCTGGAGCCGGTCCTCAATCGGAGGACGATCTTAAAGATGAGTTA" +
        "TAAGACTGCAAAACCTTTGTGTAAATCTGTGGAACATTTCTTTGACT" +
        "GGTGATACTTAATTTTTAAGTCAGTATTTATATATTTAAAAACAAAA" +
        "AACCTATACATCTGAGAAGGAAATTTGTTCCTTTTTTTCAATTTAAA" +
        "ATTTGAGTTTTTTCTTGTTTCATAAAATGTTCATTCCGCAGTTTATA" +
        "AAGTTAATTTAAAAAACAAAAACAAAAATAAAAGACTTTGTTAACTA" +
        "AGAAATTTATAATTTATTTGTTACTTTTTTATTTAATAATTTTTTTA" +
        "GTGAATTGGGAATTGATGAATTACATTCAGCATTGAAAATTTATTGG" +
        "TACCGTGTATTATAATTAATGTTGTCTGTAATTTATATAATTTCGTT" +
        "TCATTAGGTTTTTGTTTGTCAGTTGGGCTCAATCCCAAAATTTGAGA" +
        "ACATTCTGAAGGTGTGATAATAAAAGTTTCTTTATTTAAA";

    var ex_peptide = ">CLEC010822-PA:polypeptide ,Heat shock protein 70-2\n" +
        "MILHFLVLLFASALAADEKNKDVGTVVGIDLGTTYSCVGVYKNGRVEIIANDQ" +
        "GNRITPSYVAFTSEGERLIGDAAKNQLTTNPENTVFDAKRLIGREWTDSTVQD" +
        "DIKFFPFKVLEKNSKPHIQVSTSQGNKMFAPEEISAMVLGKMKETAEAYLGKK" +
        "VTHAVVTVPAYFNDAQRQATKDAGTISGLNVMRIINEPTAAAIAYGLDKKEGE" +
        "KNVLVFDLGGGTFDVSLLTIDNGVFEVVSTNGDTHLGGEDFDQRVMDHFIKLY" +
        "KKKKGKDIRKDNRAVQKLRREVEKAKRALSSSHQVRIEIESFYDGEDFSETLT" +
        "RAKFEELNMDLFRSTMKPVQKVLEDADMNKKDVDEIVLVGGSTRIPKVQALVK" +
        "EFFNGKEPSRGINPDEAVAYGAAVQAGVLSGEQDTDSIVLLDVNPLTLGIETV" +
        "GGVMTKLIPRNTVIPTKKSQIFSTASDNQHTVTIQVYEGERPMTKDNHLLGKF" +
        "DLTGIPPAPRGVPQIEVTFEIDANGILQVSAEDKGTGNREKIVITNDQNRLTP" +
        "DDIDRMIKDAEKFADDDKKLKERVEARNELESYAYSLKNQLADKDKFGSKVTD" +
        "SDKAKMEKAIEEKIKWLDENQDADSEAFKKQKKELEDVVQPIISKLYQGGAPP" +
        "PPGAGPQSEDDLKDEL*\n" +
        ">OFAS004830-PA:polypeptide ,Heat shock protein 70-2\n" +
        "MAAGGSRPTRPAVGIDLGTTYSCVGYFDKGRVEIIANDQGNRVTPSYVAFTET" +
        "DRIVGDAARGQAIMNPSNTVYDAKRLIGRKFDDPSVQADRKMWPFKVASKEGK" +
        "PMIEVTYKGETRQFFPEEISSMVLSKMRETAESYIGKKVSNAVVTVPAYFNDS" +
        "QRQATKDSGTIAGLNVLRIINEPTAAAVAYGLDKKGSGEINVLIFDLGGGTFD" +
        "VSVLTIADGLFEVKATAGDTHLGGADFDNRMVQYFLEEFKRKTKKEVNDNKRA" +
        "LRRLQAACERAKRVLSTATQATVEIDSFVDGIDLYSAVSRAKFEEINSDLFRG" +
        "TLGPVEKAIRDSKIPKNRIDEIVLVGGSTRIPKIQSLLVEYFNGKELNKTINP" +
        "DEAVAYGAAVQAAIIVGDTSDEVKDVLLLDVTPLSLGIETAGGIMTNLIPRNT" +
        "TIPVKHSQIFSTYSDNQPGVLIQVYEGERAMTKDNNLLGTFELRGFPPAPRGV" +
        "PQIEVAFDVDANGILNVTAQEMSTKKTSKITITNDKGRLTKAQIEKMVKEAER" +
        "YKSEDTAARETAEAKNGLESYCYAMKNSVEEAANLGRVTEDEMKSVVRKCNET" +
        "IMWIEANRSATKMEFEKKMRETESVCKPIATKILSRGTQQNNAGGGTPTNERG" +
        "PVIEEAD\n" +
        ">OFAS004738-PA:polypeptide ,Heat shock protein 70-1\n" +
        "MPAIGIDLGTTYSCVGVWQHGKVEIIANDQGNRTTPSYVAFSDTERLIGDAAK" +
        "NQVAMNPQNTVFDAKRLIGRKYDDPKIQDDLKHWPFRVVDCSSKPKIQVEYKG" +
        "ETKTFAPEEISSMVLVKMKETAEAYLGGTVRDAVITVPAYFNDSQRQATKDAG" +
        "AIAGLNVLRIINEPTAAALAYGLDKNLKGERNVLIFDLGGGTFDGPREQDHSL" +
        "KGERNVLIFDLGGGTFDVSILTIDEGSLFEVKSTAGDTHLGGEDFDNRLVNHL" +
        "AEEFKRKYRKDLKTNPRALRRLRTAAERAKRTLSSSTEASIEIDALFEGVDFY" +
        "TKITRARFEELCSDLFRSTLQPVEKALQDAKLDKGLIHDVVLVGGSTRIPKIQ" +
        "NLLQNFFNGKSLNMSINPDEAVAYGAAVQAAILSGDQSSKIQDVLLVDVAPLS" +
        "LGIETAGGVMTKIIERNTRI";
    
    $('#exp_nucleotide').click(function() {
        $('#blastTxt').val(ex_nucleotide);
        $('#blastTxt').keyup();
    });
    
    $('#exp_peptide').click(function() {
        $('#blastTxt').val(ex_peptide);
        $('#blastTxt').keyup();
    });

    // load file into textarea
    $('#blastFile').change(function(evt) {
        if (window.File && window.FileReader) {
            var f = evt.target.files[0];
            // console.log(f.type);
            if (f && (f.type.match('text.*') || f.type == '')) {
                var r = new FileReader();
                r.onload = function(e) {
                    var contents = e.target.result;
                    $('#blastTxt').val(contents);
                    $('#blastTxt').keyup();
                }
                r.readAsText(f);
            }
        }
    });

    // blast program descriptions for labels and their radio buttons
    $('.blastn').mouseover(function() {
        $('#blastProgramDescription').text('blastn - Nucleotide vs. Nucleotide');
    });
    $('.blastp').mouseover(function() {
        $('#blastProgramDescription').text('blastp - Peptide vs. Peptide');
    });
    $('.blastx').mouseover(function() {
        $('#blastProgramDescription').text('blastx - Translated Nucleotide vs. Peptide');
    });
    $('#programs').mouseleave(function() {
        $('.' + $('input.program:checked').val()).mouseover();
    });



    function sum(obj) {
        var sum = 0;
        for(var el in obj) {
            if(obj.hasOwnProperty(el)) {
                sum += parseFloat(obj[el]);
            }
        }
        return sum;
    }

    function filter_key(obj, test) {
        var result = {}, key;
        for (key in obj) {
            if (obj.hasOwnProperty(key) && test(key)) {
                result[key] = obj[key];
            }
        }
        return result;
    }

    var parseTextarea = _.debounce(function () {
    // var parseTextarea = function () {
        // parse only the first 100 chars for speed
        // console.log($('#blastTxt').val().substring(0, 1000).match(/[^\r\n]/g));
        // console.log($('#blastTxt').val().substring(0, 1000).match(/[^\r\n]+/g));
        var lines = $('#blastTxt').val().substring(0, 1000).match(/[^\r\n]+/g);
        if (lines == null) {
            setQueryType('');
            return;
        }
        var line_count = lines.length;
        var seq_count = 0;
        var alphabets = {};
        // http://www.ncbi.nlm.nih.gov/BLAST/blastcgihelp.shtml
        var normal_nucleic_codes = 'ATCGN';
        var valid_amino_codes = 'ABCDEFGHIKLMNPQRSTUVWXYZ*';
        var amino_only_codes = 'EFILPQZX*';
        for (var i = 0; i < line_count; i++) {
            //console.log(i + ' ' + lines[i]);
            var line = $.trim(lines[i]).toUpperCase();
            if (line[0] == '>') {
                seq_count++;
            } else {
                // check_alphabet(line);
                for (var j = 0; j < line.length; j++) {
                    if (!(line[j] in alphabets)) {
                        alphabets[line[j]] = 1;
                    } else {
                        alphabets[line[j]]++;
                    }
                }
            }
        }
        // console.log(alphabets);
        var valid_amino_count = sum(filter_key(alphabets, function (key) {
            return valid_amino_codes.indexOf(key) != -1;
        }));
        var amino_only_count = sum(filter_key(alphabets, function (key) {
            return amino_only_codes.indexOf(key) != -1;
        }));
        var normal_nucleic_count = sum(filter_key(alphabets, function (key) {
            return normal_nucleic_codes.indexOf(key) != -1;
        }));
        var total_count = sum(alphabets);
        // Too many degenerate codes within an input nucleotide query will cause blast.cgi to
        // reject the input. For protein queries, too many nucleotide-like code (A,C,G,T,N) may also
        // cause similar rejection.
        // http://www.ncbi.nlm.nih.gov/BLAST/blastcgihelp.shtml
        if (total_count == 0) {
            setQueryType('');
        } else if ((normal_nucleic_count / total_count) > 0.6 && amino_only_count == 0) {
            setQueryType('nucleotide');
        } else if (valid_amino_count == total_count) {
            setQueryType('peptide');
        } else {
            setQueryType('invalid');
        }
        // console.log(query_type, normal_nucleic_count, total_count);
    // };
    }, 30);
    $('#blastTxt').keyup(parseTextarea);

    var query_type = '';
    function setQueryType(qtype) {
        query_type = qtype;
        if (qtype == '') {
            $('.enter-query-text').html('Enter query sequence(s) below in <a target="_blank" href="https://en.wikipedia.org/wiki/FASTA_format" class="fasta">FASTA</a> format:');
            $('.enter-query-text').attr('style', 'color:default')
        } else if (qtype == 'invalid') {
            $('.enter-query-text').html('Your sequence is invalid:');
            $('.enter-query-text').attr('style', 'color:red');
        } else if (qtype == 'nucleotide') {
            $('.enter-query-text').html('Your sequence is detected as nucleotide:');
            $('.enter-query-text').attr('style', 'color:blue');
        } else if (qtype == 'peptide') {
            $('.enter-query-text').html('Your sequence is detected as peptide:');
            $('.enter-query-text').attr('style', 'color:blue');
        }
        chooseProgram();
    }

    var program_selected = 'blastn';
    var chooseProgram = _.debounce(function () {
    // var chooseProgram = function () {
        $('.program').prop('disabled', false).removeClass('disabled-radio');
        $('.program').attr('style', 'color:default');
        if (query_type == 'nucleotide') {
            $('.blastp').prop('disabled', true).addClass('disabled-radio');
            $('.blastp').attr('style', 'color:lightgray');
            // $('.tblastn').prop('disabled', true).addClass('disabled-radio');
        } else if (query_type == 'peptide') {
            $('.blastn').prop('disabled', true).addClass('disabled-radio');
            $('.blastn').attr('style', 'color:lightgray');
            $('.blastx').prop('disabled', true).addClass('disabled-radio');
            $('.blastx').attr('style', 'color:lightgray');
            // $('.tblastx').prop('disabled', true).addClass('disabled-radio');
        }
        // query_type = ''; //issue 403
        // select first non disabled option
        $('input.program:not([disabled])').first().prop('checked', true);
        program_selected = $('input.program:not([disabled])').first().val();
        $('.' + program_selected).mouseover();
        add_blast_options(program_selected.toUpperCase());                           //BLAST option//
    // };
    }, 30);

    $('.btn_reset').click(function() {
        // $('#blastTxt').val('');
        // $('blastTxt').keyup();
        setQueryType('');
        chooseProgram();
        // alert('11');
        // add_blast_options('BLASTN');
        // $('label.error').remove();
        // $('#MainBlastForm')[0].reset();
    });

    function add_blast_options(blast_program) {
        // $('#blast_title').html(blast_program+' Options');   //Show the option title
        if(document.getElementById('options-blast').style.display != "block"){
            document.getElementById('blast_title').innerHTML = '+ ' + blast_program + ' Options' 
        }
        else{
            document.getElementById('blast_title').innerHTML = '- ' + blast_program + ' Options'
        }
        // $('#options-blast label.error').remove();
        // $('.parms').hide().addClass('unselected_parms');
        // $('.' + blast_program.toLowerCase() + '-parms').show();
        // $('.' + blast_program.toLowerCase() + '-parms').removeClass('unselected_parms');
        $('.parms').attr('style','display: none;')
        $('.' + blast_program.toLowerCase() + '-parms').attr('style','display: block;')

        $('.chk_low_complexity').change();
        $('.chk_soft_masking').change();
    }

    $('.chk_low_complexity').change(function() {
        if ($('#'+$('input.program:checked').val()+'_chk_low_complexity').is(':checked')) {
            $('#low_complexity_hidden').val('yes');
        }else {
            $('#low_complexity_hidden').val('no');
        }
    });

    $('.chk_soft_masking').change(function() {
        if ($('#'+$('input.program:checked').val()+'_chk_soft_masking').is(':checked')) {
            $('#soft_masking_hidden').val('true');
        }else {
            $('#soft_masking_hidden').val('false');
        }
    });

    $('input.program:radio').click(function() {
        add_blast_options($('input.program:checked').val().toUpperCase());
    });



    //prevention of cache pages
    // $(window).unload(function () { });

});

// function judge(){
//     // var blast_content = document.getElementById('blastTxt').value;
//     var content = $('input').val()
//     if(content == ''){
//         alert('Can not be empty');
//         return false;//此处return false;即不会提交表单，一般验证表单数据不符合要求使用
//     }
// }

function click_show(divDisplay){
    blast_program = $('input.program:not([disabled])').first().val().toUpperCase();
    if(document.getElementById(divDisplay).style.display != "block"){
        document.getElementById(divDisplay).style.display = "block";
        document.getElementById('blast_title').innerHTML = '- ' + blast_program + ' Options'
    }
    else{
        document.getElementById(divDisplay).style.display = "none";
        document.getElementById('blast_title').innerHTML = '+ ' + blast_program + ' Options'
    }
}
	
// function seting(){
//     // var myselect=document.getElementById("program");
//     // var index=myselect.selectedIndex;
//     // alert(index);
//     var radio_tag = document.getElementsByName("program");
//     for(var i=0;i<radio_tag.length;i++){
//         if(radio_tag[i].checked){
//             var checkvalue = radio_tag[i].value;
//             // alert(checkvalue);
//         }
//     }
//     // if (myselect.options[index].value == "Blastp"){
//     if (checkvalue == "Blastp"){
//         var str=">sp|O00204|ST2B1_HUMAN Sulfotransferase family cytosolic 2B member 1 OS=Homo sapiens GN=SULT2B1 PE=1 SV=2\n"+
// 		"MDGPAEPQIPGLWDTYEDDISEISQKLPGEYFRYKGVPFPVGLYSLESISLAENTQDVRD\n"+
// 		"DDIFIITYPKSGTTWMIEIICLILKEGDPSWIRSVPIWERAPWCETIVGAFSLPDQYSPR\n"+
// 		"LMSSHLPIQIFTKAFFSSKAKVIYMGRNPRDVVVSLYHYSKIAGQLKDPGTPDQFLRDFL\n"+
// 		"KGEVQFGSWFDHIKGWLRMKGKDNFLFITYEELQQDLQGSVERICGFLGRPLGKEALGSV\n"+
// 		"VAHSTFSAMKANTMSNYTLLPPSLLDHRRGAFLRKGVCGDWKNHFTVAQSEAFDRAYRKQ\n"+
// 		"MRGMPTFPWDEDPEEDGSPDPEPSPEPEPKPSLEPNTSLEREPRPNSSPSPSPGQASETP\n"+
// 		"HPRPS\n";
//         document.getElementById("blastTxt").value=str;
//     }
//     // if (myselect.options[index].text == "blastn"){
//     if (checkvalue == "Blastn"){
//         var str=">sp|O00204|ST2B1_HUMAN Sulfotransferase family cytosolic 2B member 1 OS=Homo sapiens GN=SULT2B1 PE=1 SV=2\n"+
// 		"MDGPAEPQIPGLWDTYEDDISEISQKLPGEYFRYKGVPFPVGLYSLESISLAENTQDVRD\n"+
// 		"DDIFIITYPKSGTTWMIEIICLILKEGDPSWIRSVPIWERAPWCETIVGAFSLPDQYSPR\n"+
// 		"LMSSHLPIQIFTKAFFSSKAKVIYMGRNPRDVVVSLYHYSKIAGQLKDPGTPDQFLRDFL\n"+
// 		"KGEVQFGSWFDHIKGWLRMKGKDNFLFITYEELQQDLQGSVERICGFLGRPLGKEALGSV\n"+
//         "VAHSTFSAMKANTMSNYTLLPPSLLDHRRGAFLRKGVCGDWKNHFTVAQSEAFDRAYRKQ\n"+
// 		"MRGMPTFPWDEDPEEDGSPDPEPSPEPEPKPSLEPNTSLEREPRPNSSPSPSPGQASETP\n"+
// 		"HPRP\n";
//         document.getElementById("blastTxt").value=str;
//     }
//     // if (myselect.options[index].value == "Blastx"){
//     if (checkvalue == "Blastx"){
//         var str=">sp|O00204|ST2B1_HUMAN Sulfotransferase family cytosolic 2B member 1 OS=Homo sapiens GN=SULT2B1 PE=1 SV=2\n"+
// 		"MDGPAEPQIPGLWDTYEDDISEISQKLPGEYFRYKGVPFPVGLYSLESISLAENTQDVRD\n"+
// 		"DDIFIITYPKSGTTWMIEIICLILKEGDPSWIRSVPIWERAPWCETIVGAFSLPDQYSPR\n"+
// 		"LMSSHLPIQIFTKAFFSSKAKVIYMGRNPRDVVVSLYHYSKIAGQLKDPGTPDQFLRDFL\n"+
// 		"KGEVQFGSWFDHIKGWLRMKGKDNFLFITYEELQQDLQGSVERICGFLGRPLGKEALGSV\n"+
// 		"VAHSTFSAMKANTMSNYTLLPPSLLDHRRGAFLRKGVCGDWKNHFTVAQSEAFDRAYRKQ\n"+
// 		"MRGMPTFPWDEDPEEDGSPDPEPSPEPEPKPSLEPNTSLEREPRPNSSPSPSPGQASETP\n"+
// 		"HPR\n";
//         document.getElementById("blastTxt").value=str;
//     }
// }



// function judge(){
//     var radio_tag = document.getElementsByName("condition");
//     for(var i=0;i<radio_tag.length;i++){
//         if(radio_tag[i].checked){
//             var checkvalue = radio_tag[i].value;
//             // alert(checkvalue);
//         }
//     }
//     // var submitBtn = document.getElementById("submit");
//     if(checkvalue == 'txt'){
//         var blast_content = document.getElementById('blastTxt').value;
//         if(blast_content == ''){
//             alert('Can not be empty');
//             return false;//此处return false;即不会提交表单，一般验证表单数据不符合要求使用
//         }
//     }
//     if(checkvalue == 'file'){
//         var blast_content = document.getElementById('blastFile').value;
//         if(blast_content == ''){
//             alert('Can not be empty');
//             return false;
//         }
//     }
// }