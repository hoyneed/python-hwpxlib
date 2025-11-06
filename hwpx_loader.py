import jpype
import jpype.imports
import argparse
from cleaning import clean_rag_text, clean_common_noise


def hwpx_extract(hwpx_jar_path, file_path):
    try:
        ## jpype 시작
        jpype.startJVM(
            classpath=[hwpx_jar_path],
            convertStrings=True,
        )

        ## java package 가져오기
        from kr.dogfoot.hwpxlib.reader import HWPXReader
        from kr.dogfoot.hwpxlib.tool.textextractor import (
            TextExtractor,
            TextMarks,
            TextExtractMethod,
        )

        hwpx_file = HWPXReader.fromFilepath(file_path)
        text_extract_method = TextExtractMethod.InsertControlTextBetweenParagraphText
        text_marks = (
            TextMarks()
            .lineBreakAnd("\n")
            .paraSeparatorAnd("\n\n")
            .tableStartAnd("<table>\n")
            .tableEndAnd("\n</table>")
            .tabAnd("\t")
            .containerStartAnd("\n\n")
            .containerEndAnd("\n\n")
            .fieldStartAnd("")
            .fieldEndAnd("")
        )

        # 한글 추출
        hwpxtext = TextExtractor.extract(
            hwpx_file, text_extract_method, True, text_marks
        )
        hwpxtext = clean_rag_text(hwpxtext)
        hwpxtext = clean_common_noise(hwpxtext)

    except Exception as e:
        hwpxtext = "Error Occurred: " + str(e)
    finally:
        jpype.shutdownJVM()
    return hwpxtext


if __name__ == "__main__":
    # 파라미터 파싱
    parser = argparse.ArgumentParser(description="Hwpx loader")
    parser.add_argument(
        "--hwpx_jar_path",
        type=str,
        default="hwpxlib-1.0.7.jar",
        help="hwpxlib jar 위치",
    )
    parser.add_argument(
        "--file_path", type=str, default="./test.hwpx", help="hwpx 파일 경로"
    )
    args = parser.parse_args()

    hwp_text = hwpx_extract(args.hwpx_jar_path, args.file_path)

    # print로 표준출력
    print(hwp_text)